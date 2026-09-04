import socket
import threading
import struct
import json

HOST = '0.0.0.0'
PORT = 5555




def recv_exact(sock, n):

    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:  # החיבור נסגר
            return None
        data += chunk
    return data


def recv_message(sock):

    header = recv_exact(sock, 4)
    if header is None:
        return None
    (length,) = struct.unpack('!I', header)
    payload = recv_exact(sock, length)
    if payload is None:
        return None
    return json.loads(payload.decode('utf-8'))


def send_message(sock, message_dict):

    payload = json.dumps(message_dict).encode('utf-8')
    header = struct.pack('!I', len(payload))
    sock.sendall(header + payload)




class Server:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.clients = []  # רשימת (socket, username)
        self.lock = threading.Lock()

    def other_client(self, sender_conn):
        with self.lock:
            for conn, username in self.clients:
                if conn is not sender_conn:
                    return conn
        return None

    def handle_client(self, conn, username):
        try:
            while True:
                msg = recv_message(conn)
                if msg is None:
                    break
                other = self.other_client(conn)
                if other:
                    try:
                        send_message(other, msg)
                    except OSError:
                        pass
        except (ConnectionResetError, OSError):
            pass
        finally:
            print(f"[SERVER] {username} התנתק")
            other = self.other_client(conn)
            if other:
                try:
                    send_message(other, {'type': 'system', 'msg': f'{username} התנתק מהצ׳אט'})
                except OSError:
                    pass
            with self.lock:
                self.clients = [(c, u) for c, u in self.clients if c is not conn]
            try:
                conn.close()
            except OSError:
                pass

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(2)
        print(f"[SERVER] מאזין על {self.host}:{self.port}")

        # מקבלים בדיוק שני לקוחות
        while len(self.clients) < 2:
            conn, addr = server_socket.accept()
            join_msg = recv_message(conn)
            if join_msg is None or join_msg.get('type') != 'join':
                conn.close()
                continue
            username = join_msg.get('user', f'User{len(self.clients) + 1}')
            with self.lock:
                self.clients.append((conn, username))
            print(f"[SERVER] {username} התחבר ({len(self.clients)}/2)")
            threading.Thread(target=self.handle_client, args=(conn, username), daemon=True).start()

        with self.lock:
            for conn, username in self.clients:
                send_message(conn, {'type': 'system', 'msg': 'שני המשתמשים מחוברים - אפשר להתחיל לשוחח!'})

        print("[SERVER] שני הלקוחות מחוברים, מעביר הודעות ביניהם...")


if __name__ == '__main__':
    server = Server()
    server.start()
    threading.Event().wait()

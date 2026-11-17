import socket
import threading
import json
from db_manager import DatabaseManager


class Server():
    def __init__(self):
        self.db = DatabaseManager()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 5555))
        server_socket.listen()

        while True:
            client_connection, client_address = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_connection, client_address)).start()

    def handle_client(self, client_socket, client_address):
        print("Client ", client_address, " started new thread")

        while True:
            try:
                raw_data = client_socket.recv(1024).decode()
                print(raw_data)
                if not raw_data:
                    break

                request = json.loads(raw_data)
                action = request.get("action")

                if action == "register":
                    username = request.get("username")
                    password = request.get("password")
                    interests = request.get("interests", [])

                    success, message = self.db.register_user(username, password, interests)

                    response_payload = {
                        "status": "success" if success else "error",
                        "message": message
                    }
                    client_socket.send(json.dumps(response_payload).encode())

                elif action == "login":
                    username = request.get("username")
                    password = request.get("password")

                    success, message = self.db.validate_login(username, password)

                    response_payload = {
                        "status": "success" if success else "error",
                        "message": message
                    }
                    client_socket.send(json.dumps(response_payload).encode())

            except json.JSONDecodeError:
                error_response = {"status": "error", "message": "Invalid JSON format"}
                client_socket.send(json.dumps(error_response).encode())
            except ConnectionResetError:
                break

        client_socket.close()


if __name__ == '__main__':
    server = Server()
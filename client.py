import socket
import struct
import json
import threading
import queue
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555




def recv_exact(sock, n):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
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




class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("צ'אט מוצפן")
        self.root.geometry("500x520")
        self.sock = None
        self.username = None
        self.incoming = queue.Queue()
        self.connected = False

        self.build_gui()
        self.ask_connection_details()

    def build_gui(self):
        self.status_var = tk.StringVar(value="לא מחובר")
        tk.Label(self.root, textvariable=self.status_var, anchor='w', fg='gray').pack(
            fill='x', padx=8, pady=(8, 0))

        self.chat_area = scrolledtext.ScrolledText(self.root, state='disabled', wrap='word')
        self.chat_area.pack(fill='both', expand=True, padx=8, pady=8)

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill='x', padx=8, pady=(0, 8))

        self.entry = tk.Entry(bottom_frame)
        self.entry.pack(side='left', fill='x', expand=True)
        self.entry.bind('<Return>', lambda e: self.send_message())

        tk.Button(bottom_frame, text="שלח", command=self.send_message).pack(side='right', padx=(8, 0))

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def ask_connection_details(self):
        self.username = simpledialog.askstring("שם משתמש", "הכנס שם משתמש:", parent=self.root) or "אנונימי"
        host = simpledialog.askstring("שרת", "כתובת IP של השרת:",
                                      initialvalue=SERVER_HOST, parent=self.root) or SERVER_HOST
        port_str = simpledialog.askstring("שרת", "מספר פורט:",
                                          initialvalue=str(SERVER_PORT), parent=self.root) or str(SERVER_PORT)
        try:
            port = int(port_str)
        except ValueError:
            port = SERVER_PORT
        self.connect(host, port)

    def connect(self, host, port):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            send_message(self.sock, {'type': 'join', 'user': self.username})
        except OSError as e:
            messagebox.showerror("שגיאת חיבור", f"לא ניתן להתחבר לשרת: {e}")
            self.root.destroy()
            return

        self.connected = True
        self.status_var.set(f"מחובר כ-{self.username} — ממתין למשתמש נוסף...")

        threading.Thread(target=self.receive_loop, daemon=True).start()
        self.root.after(100, self.poll_queue)

    def receive_loop(self):

        while self.connected:
            msg = recv_message(self.sock)
            if msg is None:
                self.incoming.put({'type': 'system', 'msg': 'החיבור לשרת נותק'})
                self.connected = False
                break
            self.incoming.put(msg)

    def poll_queue(self):

        try:
            while True:
                msg = self.incoming.get_nowait()
                self.display_message(msg)
        except queue.Empty:
            pass
        if self.connected:
            self.root.after(100, self.poll_queue)

    def display_message(self, msg):
        self.chat_area.configure(state='normal')
        if msg.get('type') == 'system':
            text = msg.get('msg', '')
            self.chat_area.insert('end', f"* {text} *\n")
            if 'מחוברים' in text:
                self.status_var.set(f"מחובר כ-{self.username}")
        else:
            sender = msg.get('user', '???')
            text = msg.get('msg', '')
            self.chat_area.insert('end', f"{sender}: {text}\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.see('end')

    def send_message(self):
        text = self.entry.get().strip()
        if not text or not self.connected:
            return
        try:
            send_message(self.sock, {'type': 'text', 'user': self.username, 'msg': text})
            self.display_message({'type': 'text', 'user': f"{self.username} (אני)", 'msg': text})
            self.entry.delete(0, 'end')
        except OSError:
            messagebox.showerror("שגיאה", "שליחת ההודעה נכשלה — החיבור נותק")
            self.connected = False

    def on_close(self):
        self.connected = False
        try:
            if self.sock:
                self.sock.close()
        except OSError:
            pass
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
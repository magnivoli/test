import socket
import threading
import json

class Client():
    def __init__(self, response_callback=None):
        self.response_callback = response_callback
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 5555))
        print("Connected to Server")

        self.is_running = True
        self.listen_thread = threading.Thread(target=self.listen_to_server, daemon=True)
        self.listen_thread.start()

    def send_message(self, message_string):
        self.client_socket.send(message_string.encode())

    def listen_to_server(self):
        while self.is_running:
            try:
                raw_data = self.client_socket.recv(1024).decode()
                if not raw_data:
                    break

                response = json.loads(raw_data)
                if self.response_callback:
                    self.response_callback(response)

            except (ConnectionResetError, json.JSONDecodeError):
                break

    def set_callback(self, callback_func):
        self.response_callback = callback_func
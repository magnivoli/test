import socket

class Client():
    client_socket = None
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 5555))
        print("Connected to Server")

    def send_message(self,message_string):
        self.client_socket.send(message_string.encode())





if __name__ == '__main__':
    client = Client()







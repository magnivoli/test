import socket
import threading

class Server():
    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 5555))
        server_socket.listen()

        while True:
            client_connection, client_address = server_socket.accept()
            threading.Thread(target= self.handle_client, args = (client_connection, client_address)).start()

    def handle_client(self,client_socket,client_address):
        print("Client ", client_address," started new thread")

        while True:
            message = client_socket.recv(1024).decode()
            print(message)

        pass





if __name__ == '__main__':
    server = Server()













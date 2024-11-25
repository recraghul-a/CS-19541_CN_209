import socket
import threading


def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

def send_messages(client_socket):
    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())

def main():
    host = '127.0.0.1'  # Replace with the server's IP address
    port = 8080  # Replace with the desired port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_messages(client_socket)

if __name__ == '__main__':
    main()
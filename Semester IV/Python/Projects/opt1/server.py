import socket
import threading

# Constants
HEADER_LENGTH = 10
HOST = socket.gethostname()  # Replace with the server IP address
PORT = 9999  # Replace with the port number that the server is listening to

# Global variables
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = {}

# Functions


def handle_client(client_socket, client_address):
    """Handles the communication with a client."""
    try:
        # Get the client's username
        username_header = client_socket.recv(HEADER_LENGTH)
        username_length = int(username_header.decode('utf-8').strip())
        username = client_socket.recv(username_length).decode('utf-8')
        clients[client_socket] = username

        # Broadcast the client's connection to all connected clients
        broadcast_message(f"{username} has joined the chat!".encode('utf-8'))

        # Receive messages from the client and broadcast them to all connected clients
        while True:
            message_header = client_socket.recv(HEADER_LENGTH)
            if not len(message_header):
                return
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            broadcast_message(f"{username}: {message}".encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()
        del clients[client_socket]
        broadcast_message(f"{username} has left the chat!".encode('utf-8'))


def broadcast_message(message):
    """Broadcasts a message to all connected clients."""
    for client_socket in clients:
        try:
            client_socket.send(message)
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            del clients[client_socket]
            broadcast_message(f"{clients[client_socket]} has left the chat!".encode('utf-8'))


# Wait for clients to connect
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address))
    client_thread.start()


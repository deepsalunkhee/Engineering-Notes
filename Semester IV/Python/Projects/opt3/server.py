import socket
import threading

# Define host and port for server
HOST = 'localhost'
PORT = 5000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Define function to handle incoming client connections
def handle_client(client_socket, client_address):
    while True:
        # Receive data from client
        data = client_socket.recv(1024)

        if not data:
            # If no data is received, the client has disconnected
            print(f"Client {client_address} has disconnected")
            break

        # Print received message and client address
        print(f"Received message from {client_address}: {data.decode()}")

        # Send message to all clients except the sender
        for sock in client_sockets:
            if sock != client_socket:
                sock.sendall(f"{client_address[0]}: {data.decode()}".encode())

    # Close client socket
    client_socket.close()

# Create a list to store client sockets
client_sockets = []

while True:
    # Wait for incoming client connections
    client_socket, client_address = server_socket.accept()

    # Add client socket to list
    client_sockets.append(client_socket)

    # Create a new thread to handle client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()


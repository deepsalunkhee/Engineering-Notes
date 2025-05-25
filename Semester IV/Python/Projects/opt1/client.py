import tkinter as tk
import socket
import threading

# Constants
HEADER_LENGTH = 10
HOST = socket.gethostname()  # Replace with the server IP address
PORT = 9999  # Replace with the port number that the server is listening to

# Global variables
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
username = ""

# Functions


def send_message(event=None):
    """Sends the message to the server."""
    global username
    message = input_field.get()
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
        input_field.delete(0, tk.END)
        if message.decode().lower() == 'exit':
            client_socket.close()
            window.quit()
        else:
            # Display the message in the chat window
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"{username}: {message.decode()}\n")
            chat_window.config(state=tk.DISABLED)
            chat_window.see(tk.END)


def receive_message():
    """Receives messages from the server and displays them in the chat window."""
    while True:
        try:
            # Receive message header
            message_header = client_socket.recv(HEADER_LENGTH)
            if not len(message_header):
                return
            # Decode message header and get message length
            message_length = int(message_header.decode('utf-8').strip())
            # Receive message
            message = client_socket.recv(message_length).decode('utf-8')
            # Display the message in the chat window
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"{message}\n")
            chat_window.config(state=tk.DISABLED)
            chat_window.see(tk.END)
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            break



def set_username():
    """Prompts the user to set their username."""
    global username
    username = input("Enter your username: ")
    if username:
        username_label.config(text=f"Logged in as: {username}")
        username_button.config(state=tk.DISABLED)
        input_field.config(state=tk.NORMAL)
        input_field.focus_set()
        receive_thread = threading.Thread(target=receive_message)
        receive_thread.start()


# GUI setup
window = tk.Tk()
window.title("Chat Room")

frame_top = tk.Frame(window)
username_label = tk.Label(frame_top, text="Please set your username.")
username_label.pack(side=tk.LEFT, padx=(10, 0))
username_button = tk.Button(
    frame_top, text="Set username", command=set_username)
username_button.pack(side=tk.LEFT, padx=(10, 0))
frame_top.pack(side=tk.TOP, pady=(10, 0))

frame_middle = tk.Frame(window)
scrollbar = tk.Scrollbar(frame_middle)
chat_window = tk.Text(frame_middle, height=20, width=50,
                      yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_window.yview)
chat_window.config(state=tk.DISABLED)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window.pack(side=tk.LEFT, fill=tk.BOTH, padx=(10, 0), pady=(10, 0))
frame_middle.pack()

frame_bottom = tk.Frame(window)
input_field = tk.Entry(frame_bottom, width=50)
input_field.pack(side=tk.LEFT, padx=(10, 0))
input_field.bind("<Return>", send_message)
send_button = tk.Button(frame_bottom, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(10, 0))
frame_bottom.pack(side=tk.BOTTOM, pady=(10, 0))

# Start the GUI loop
window.mainloop()


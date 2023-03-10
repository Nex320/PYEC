import socket
import threading
import os
from datetime import datetime

# Define host and port number
HOST = 'Your PYEC Server ip here'
PORT = YOUR PORT HERE

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect((HOST, PORT))

# Ask user to enter username
username = input("Please enter your username: ")
s.send(username.encode())
welcome_message = s.recv(1024).decode()
print(welcome_message)

# Define function to receive messages from server
def receive_messages():
    while True:
        try:
            # Receive message from server
            message = s.recv(1024).decode()
            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            # Print message to console
            print(message)
            # Re-print "Message: " text
            print("Message: ", end='', flush=True)
        except:
            # If an error occurs, close connection and exit thread
            s.close()
            break

# Start thread to receive messages from server
thread = threading.Thread(target=receive_messages)
thread.start()

# Allow user to enter and send messages to server
while True:
    message = input("Message: ")
    # Create message with current date, username, and user input
    message = f"{datetime.now().strftime('%m/%d/%Y %I:%M %p')} - {username}: {message}"
    # Send message to server
    s.send(message.encode())
import socket
import threading
import os
from datetime import datetime
import colorama
from colorama import Fore

# Define host and port number
HOST = 'iphere'
PORT = porthere

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server
    s.connect((HOST, PORT))
except ConnectionRefusedError:
    # If connection fails, display message and wait for user input
    print(Fore.RED + "I'm sorry, But the " + Fore.CYAN + "Nexwork" + Fore.RED + " cannot be reached at this moment. Please try again at a later date...")
    input(Fore.YELLOW + " \nPress the Enter key to close PYEC")
    exit()

# Ask user to enter username
username = input(Fore.YELLOW + "Please enter your username: ")
print(Fore.WHITE)
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
            if 'burgerbog' in message:
                # Split message by lines and only display lines after the one containing "burgerbog"
                message_lines = message.split('\n')
                burgerbog_index = message_lines.index('burgerbog')
                for line in message_lines[burgerbog_index+1:]:
                    print(line)
                # Display prompt to exit user list
                print('\nPress enter to exit userlist')
                # Don't show the "Message:" prompt while in user list
                continue
            else:
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
    if message.startswith('/'):
        # If message starts with slash, parse command
        if message == '/users':
            # Send text "breakaway01" to server
            s.send('breakaway01'.encode())
        else:
            # Unknown command
            print("Unknown command.")
    else:
        # Create message with current date, username, and user input
        message = f"{datetime.now().strftime('%m/%d/%Y %I:%M %p')} - {username}: {message}"
        # Send message to server
        s.send(message.encode())

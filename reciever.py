import socket
import pydirectinput

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.320', 12345))

def handle_command(command):
    if command == "left_click":
        pydirectinput.click(button='left')
    elif command == "right_click":
        pydirectinput.click(button='right')
    elif "move_pointer" in command:
        _, laser_value = command.split(":")
        move_pointer(int(laser_value))

def move_pointer(laser_value):
    if laser_value > 128:
        pydirectinput.move(10, 0)
    else:
        pydirectinput.move(-10, 0)

try:
    while True:
        data = client_socket.recv(1024).decode()
        if data:
            handle_command(data)

finally:
    client_socket.close()

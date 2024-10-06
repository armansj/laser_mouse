import machine
import socket
import time

left_click_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
right_click_button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
laser_sensor = machine.ADC(26)

# Setup socket connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.32', 12345))
server_socket.listen(1)

print("Waiting for client to connect...")
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")


def send_command(command):
    client_socket.send(command.encode())


try:
    while True:
        if not left_click_button.value():
            send_command("left_click")
            time.sleep(0.3)  # debounce

        if not right_click_button.value():
            send_command("right_click")
            time.sleep(0.3)  # debounce

        laser_value = laser_sensor.read_u16() // 256
        send_command(f"move_pointer:{laser_value}")

        time.sleep(0.1)  # Limit frequency of messages

finally:
    client_socket.close()
    server_socket.close()

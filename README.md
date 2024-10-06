# Raspberry Pi Pico W - Click and Pointer Project

This project demonstrates how to use a Raspberry Pi Pico W with two buttons acting as left and right mouse clicks and a laser sensor acting as a pointer. The Raspberry Pi Pico W communicates with a laptop using socket programming, and the laptop executes the mouse actions using Python's `pydirectinput` library.

## Features
- **Left Click**: Triggered by one button on the Raspberry Pi.
- **Right Click**: Triggered by a second button on the Raspberry Pi.
- **Pointer Movement**: The laser sensor connected to the Raspberry Pi controls the movement of the mouse pointer on the laptop.

## Hardware Requirements
- Raspberry Pi Pico W
- 2 push buttons (for left and right clicks)
- Laser sensor (for pointer control)
- Connecting wires
- Breadboard (optional)

## Software Requirements
- Python 3.x (both on Raspberry Pi Pico W and the client machine)
- `pydirectinput` library (on the client machine)

## Setup

### Server-side (Raspberry Pi Pico W)
1. Clone the repository and upload the `sender.py` script to your Raspberry Pi Pico W.
2. Connect the buttons to GPIO pins and the laser sensor to an ADC pin on the Raspberry Pi.
3. Ensure your Raspberry Pi Pico W is connected to the same network as your client machine.
4. Run the `server.py` script on the Raspberry Pi Pico W.

```bash
python sender.py

import serial
import serial.tools.list_ports
import random
import time
import sys
from termcolor import colored


class ArduinoMouse:
    def __init__(self, filter_length=3):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 1
        self.serial_port.port = self.find_serial_port()
        self.filter_length = filter_length
        self.x_history = [0] * filter_length
        self.y_history = [0] * filter_length
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(colored('[Error]', 'red'), colored(
                'FTNAIMZ is already open or serial port in use by another app. Close FTNAIMZ and other apps before retrying.',
                'white'))
            time.sleep(10)
            sys.exit()

    def find_serial_port(self):
        port = next((port for port in serial.tools.list_ports.comports() if "Arduino" in port.description), None)
        if port is not None:
            return port.device
        else:
            print(colored('[Error]', 'red'), colored(
                'Unable to find serial port or the Arduino device is with different name. Please check its connection and try again.',
                'white'))
            time.sleep(10)
            sys.exit()

    def move(self, x, y):
        self.x_history.append(x)
        self.y_history.append(y)

        self.x_history.pop(0)
        self.y_history.pop(0)

        smooth_x = int(sum(self.x_history) / self.filter_length)
        smooth_y = int(sum(self.y_history) / self.filter_length)

        finalx = smooth_x + 256 if smooth_x < 0 else smooth_x
        finaly = smooth_y + 256 if smooth_y < 0 else smooth_y
        self.serial_port.write(b"M" + bytes([int(finalx), int(finaly)]))

    def flick(self, x, y):
        x = x + 256 if x < 0 else x
        y = y + 256 if y < 0 else y
        self.serial_port.write(b"M" + bytes([int(x), int(y)]))

    def click(self):
        delay = random.uniform(0.01, 0.1)
        self.serial_port.write(b"C")
        time.sleep(delay)

    def close(self):
        self.serial_port.close()

    def __del__(self):
        self.close()
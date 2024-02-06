import os
import time
import keyboard
import pyautogui
from termcolor import colored
from ftnaimz import Ftnaim

# Settings
TOGGLE_KEY = 'F1'  # Toggle on/off FTNAIM key
XFOV = 100  # X-Axis FOV
YFOV = 50  # Y-Axis FOV
FLICKSPEED = 1.07437623  # Default flick speed
MOVESPEED = 1 / 5  # Default move speed

monitor = pyautogui.size()
CENTER_X, CENTER_Y = monitor.width // 2, monitor.height // 2

senstitle = colored('''
░██████╗███████╗███╗░░██╗░██████╗░█████╗░
██╔════╝██╔════╝████╗░██║██╔════╝██╔══██╗
╚█████╗░█████╗░░██╔██╗██║╚█████╗░╚═╝███╔╝
░╚═══██╗██╔══╝░░██║╚████║░╚═══██╗░░░╚══╝░
███████╔╝███████╗██║░╚███║██████╔╝░░░██╗░░
╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░
''', 'magenta')

ftntitle = colored('''
███████╗████████╗███╗░░██╗  ░▄▄▄▄░    ░█████╗░██╗███╗░░░███╗███████╗
██╔════╝╚══██╔══╝████╗░██║  ▀▀▄██►    ██╔══██╗██║████╗░████║╚════██║
█████╗░░░░░██║░░░██╔██╗██║  ▀▀███►    ███████║██║██╔████╔██║░░███╔═╝
██╔══╝░░░░░██║░░░██║╚████║  ░▀███►░█► ██╔══██║██║██║╚██╔╝██║██╔══╝░░
██║░░░░░░░░██║░░░██║░╚███║  ▒▄████▀▀  ██║░░██║██║██║░╚═╝░██║███████╗
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚══╝            ╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝
FTN AIMZ - v1.0''', 'magenta')


def calculate_settings(sensitivity):
    global FLICKSPEED, MOVESPEED
    FLICKSPEED = 1.07437623 * (sensitivity ** -0.9936827126)  # Calculate flick speed
    MOVESPEED = 1 / (5 * sensitivity)  # Calculate move speed


def main():
    os.system('title ftnaimbot')

    print(senstitle)
    sensitivity = float(input(colored("Enter your sensitivity: ", 'magenta')))
    calculate_settings(sensitivity)

    os.system("cls")

    ftnaimbot = Ftnaim(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, MOVESPEED)

    print(ftntitle)
    print(colored('Discord:', 'magenta'), colored('lostspaceship', 'magenta'))
    print(colored('GitHub:', 'magenta'), end=' ')
    print(colored('https://github.com/lostspaceship', 'magenta', attrs=['underline']))

    print()
    print(colored('[Info]', 'magenta'), colored('Set enemies to', 'white'), colored('Purple', 'magenta'))
    print(colored('[Info]', 'magenta'), colored(f'Press {TOGGLE_KEY} to toggle FTN AIM', 'white'))
    print(colored('[Info]', 'magenta'), colored(f'Press F2 to toggle Detection Window', 'white'))
    print(colored('[Info]', 'magenta'), colored('RightMB', 'magenta'), colored('= Aimbot', 'white'))
    print(colored('[Info]', 'magenta'), colored('LeftAlt', 'magenta'), colored('= Triggerbot', 'white'))
    status = 'Disabled'

    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                ftnaimbot.toggle()
                status = 'Enabled ' if ftnaimbot.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "magenta")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'magenta'), colored('Exiting...', 'white') + '\n')
    finally:
        ftnaimbot.close()


if __name__ == '__main__':
    main()
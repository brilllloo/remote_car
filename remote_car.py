import time
import keyboard

from TCPClient import TCPClient
from Command import COMMAND as cmd


def GoForward():
    tcp.sendData(cmd.CMD_FORWARD + str(100))
    time.sleep(0.1)
    tcp.sendData(cmd.CMD_STOP)
    print("Forward.")

def GoBackward():
    tcp.sendData(cmd.CMD_BACKWARD + str(100))
    time.sleep(0.1)
    tcp.sendData(cmd.CMD_STOP)
    print("Backward.")

def GoLeft():
    tcp.sendData(cmd.CMD_TURN_LEFT + str(8))
    """time.sleep(0.1)"""
    tcp.sendData(cmd.CMD_STOP)
    print("Left.")

def GoRight():
    tcp.sendData(cmd.CMD_TURN_LEFT + str(8))
    time.sleep(0.1)
    tcp.sendData(cmd.CMD_STOP)
    print("Left.")

print("REMOTE CAR")
print("-------------------")

SERVER_IP="bbs-smartcar"

SERVO_MIN_ANGLE = 0
SERVO_MAX_ANGLE = 180

tcp = TCPClient()

print("Connecting ...", SERVER_IP)

try:
    tcp.connectToServer(address = (SERVER_IP, 12345))
except Exception as e:
    print("Connection to server", SERVER_IP, "failed!")
    exit(1)


print("Connection successful!")

''' Center wheels '''
tcp.sendData(cmd.CMD_TURN_LEFT + str(50))

while True:
    if keyboard.is_pressed("w"):
        GoForward()

    elif keyboard.is_pressed("s"):
        GoBackward()

    elif keyboard.is_pressed("a"):
        GoLeft()

    elif keyboard.is_pressed("d"):
        GoRight()

    elif keyboard.is_pressed("Esc"):
        break

tcp.sendData(cmd.CMD_STOP)

tcp.disConnect()

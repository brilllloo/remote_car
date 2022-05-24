import time
import ultrasonic
import keyboard

from TCPClient import TCPClient
from Command import COMMAND as cmd
from time import sleep

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

print("center wheels")
tcp.sendData(cmd.CMD_TURN_LEFT + str(8))


print("green led - program starting")
tcp.sendData(cmd.CMD_RGB_G)
time.sleep(1)
tcp.sendData(cmd.CMD_RGB_G)

tcp.sendData(cmd.CMD_TURN_LEFT + str(8))

        
""" end of code """


print("blue led - program stopped")
tcp.sendData(cmd.CMD_RGB_B)
time.sleep(1)
tcp.sendData(cmd.CMD_RGB_B)

tcp.sendData(cmd.CMD_STOP)

tcp.disConnect()

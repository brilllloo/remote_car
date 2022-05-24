import RPi.GPIO as GPIO
import time
import ultrasonic

from TCPClient import TCPClient
from Command import COMMAND as cmd
from gpiozero import LED, Button
from time import sleep

print("Test1 demo pgrogram")
print("-------------------")

followerL = 25
GPIO.setup(followerL, GPIO.IN)

followerR = 17
GPIO.setup(followerR, GPIO.IN)

SERVER_IP="localhost"

SERVO_MIN_ANGLE = 0
SERVO_MAX_ANGLE = 180

tcp = TCPClient()

print("Connecting ...", SERVER_IP)

try:
    tcp.connectToServer(address = (SERVER_IP, 12345))
except Exception as e:
    print("Connection to server", SERVER_IP, "failed!")
    exit(1)

print("Connection Successful !")

print("center wheels")
tcp.sendData(cmd.CMD_TURN_LEFT + str(8))


print("green led - program starting")
tcp.sendData(cmd.CMD_RGB_G)
time.sleep(1)
tcp.sendData(cmd.CMD_RGB_G)
tcp.sendData(cmd.CMD_TURN_LEFT + str(8))
 
for i in range(100):
    if GPIO.input(followerL) != 0:
        print('The sensor is seeing a blackL surface')
    else:
        print('The sensor is seeing a whiteL surface')
        
    if GPIO.input(followerR) != 0:
        print('The sensor is seeing a blackR surface')
    else:
        print('The sensor is seeing a whiteR surface')

    if GPIO.input(followerL) != 0 and GPIO.input(followerR) != 0:
        tcp.sendData(cmd.CMD_FORWARD + str(25))
    elif GPIO.input(followerL) == 0 and GPIO.input(followerR) != 0:
        tcp.sendData(cmd.CMD_TURN_RIGHT + str(35))
        tcp.sendData(cmd.CMD_FORWARD + str(25))
    elif GPIO.input(followerL) != 0 and GPIO.input(followerR) == 0:
        tcp.sendData(cmd.CMD_TURN_LEFT + str(35))
        tcp.sendData(cmd.CMD_FORWARD + str(25))
    else:
        tcp.sendData(cmd.CMD_TURN_LEFT + str(8))
        tcp.sendData(cmd.CMD_BACKWARD + str(37))

    time.sleep(0.05)


"""for i in range (20):
    distance = ultrasonic.getSonar()
    print(distance)
    if (distance > 10):
        print("forward")
        tcp.sendData(cmd.CMD_FORWARD + str(50))
        time.sleep(1)
    else:
        print("backward")
        tcp.sendData(cmd.CMD_RGB_R)
        tcp.sendData(cmd.CMD_TURN_LEFT + str(50))
        tcp.sendData(cmd.CMD_BACKWARD + str(50))
        time.sleep(1.5)
        tcp.sendData(cmd.CMD_STOP)
        tcp.sendData(cmd.CMD_TURN_LEFT + str(8))
        tcp.sendData(cmd.CMD_RGB_R)
        time.sleep(0.2)"""
        
print("blue led - program stopped")
tcp.sendData(cmd.CMD_RGB_B)
time.sleep(1)
tcp.sendData(cmd.CMD_RGB_B)

'''
for i in range (20, 100, 5):
    distance = ultrasonic.getSonar()
    print("Distance: ", distance)
    if (distance > 50):
        tcp.sendData(cmd.CMD_FORWARD + str(i))
        time.sleep(0.2)
'''
tcp.sendData(cmd.CMD_STOP)

tcp.disConnect()
GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep

def initialize():
    GPIO.setmode(GPIO.BOARD)
    # Update GPIO pins based on the provided image
    GPIO.setup(32, GPIO.OUT)  # GPIO 12
    GPIO.setup(33, GPIO.OUT)  # GPIO 13
    GPIO.setup(35, GPIO.OUT)  # GPIO 19
    GPIO.setup(36, GPIO.OUT)  # GPIO 16
    motor2 = GPIO.PWM(33, 50) # height
    motor3 = GPIO.PWM(35, 50) # distance from base
    motor4 = GPIO.PWM(36, 50) # base
    motor2.start(9)
    sleep(1)
    motor3.start(9.5)
    sleep(1)
    motor4.start(7.5)
    sleep(1)
    return {
        2: motor2,
        3: motor3,
        4: motor4
    }

def movebase(motorno, destpos, motors):  
    initposes = {
        1: 8,
        2: 9,
        3: 9.5,
        4: 7.5
    }
    initpos = initposes[motorno]
    motor = motors[motorno]
    motor.ChangeDutyCycle(destpos)
    sleep(1)


def moveondetect():
    motors = initialize()
    movebase(2, 11, motors)
    movebase(1, 11, motors)
    movebase(2, 8, motors)
    movebase(4, 11, motors)
    movebase(3, 11, motors)
    movebase(2, 11, motors)
    movebase(1, 8, motors)
    movebase(2, 9, motors)
    movebase(3, 9.5, motors)
    movebase(4, 7.5, motors)
    movebase(2, 9, motors)
    GPIO.cleanup()

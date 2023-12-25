#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

# It seems like the classes are created from smaller components to larger systems.
# Classes are created to represent actual physical system. Sometimes it can be created to a virtual state.
# It can also be created to keep component specific data organized and use them easily when required.
class Motor:
    def __init__ (self, pinFwd, pinBack, frequency=20, maxSpeed=100):
        #  Configure GPIO
        GPIO.setup (pinFwd,  GPIO.OUT)
        GPIO.setup (pinBack, GPIO.OUT)

        #  get a handle to PWM
        self._frequency = frequency
        self._maxSpeed = maxSpeed
        self._pwmFwd  = GPIO.PWM (pinFwd,  frequency)
        self._pwmBack = GPIO.PWM (pinBack, frequency)
        self.stop()

    def forwards (self, speed):
        self._move (speed)

    def backwards (self, speed):
        self._move (-speed)

    def stop (self):
        self._move (0)

    def _move (self, speed):
        #  set limits
        if speed > self._maxSpeed:
            speed = self._maxSpeed
        if speed < -self._maxSpeed:
            speed = -self._maxSpeed

        #  turn on the motors
        # here the start method is used to specify the duty cycle of the pins out. 
        # If no argument is passed to the start method, then it starts with the last set duty cycle.
        if speed < 0:
            self._pwmFwd.start(0)
            self._pwmBack.start(-speed)
        else:
            self._pwmFwd.start(speed)
            self._pwmBack.start(0)

# here the Wheelie class is subclassing the Motor class directly.
# This way the Wheelie class has 2 inherent objects every single time a Wheelie object is created.
class Wheelie:
    def __init__ (self):
        self.rightWheel = Motor (10, 9)
        self.leftWheel = Motor (8, 7)

    def stop (self):
        self.leftWheel.stop()
        self.rightWheel.stop()

    def goForward (self, speed = 100):
        self.rightWheel.forwards (speed)
        self.leftWheel.forwards (speed)

    def goBackward (self, speed = 100):
        self.rightWheel.backwards (speed)
        self.leftWheel.backwards (speed)

    def goLeft (self, speed = 100):
        self.rightWheel.backwards (speed)
        self.leftWheel.forwards (speed)

    def goRight (self, speed = 100):
        self.rightWheel.forwards (speed)
        self.leftWheel.backwards (speed)

def main():
    wheelie = Wheelie()
    wheelie.goForward()
    time.sleep(1)
    wheelie.goLeft()
    time.sleep(1)
    wheelie.goBackward(50)
    time.sleep(1)
    wheelie.goRight()
    time.sleep(1)
    wheelie.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

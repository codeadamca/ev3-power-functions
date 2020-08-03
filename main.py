#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor)
from pybricks.parameters import Port
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()

# The power functions adapter will be recognized as a standard EV3
# motor. Initilize the port using a standard EV3 motor, use the standard 
# EV3 motor code to control Power Functions motors and/or lights. 
motor = Motor(Port.A)

# Beep to start the program
ev3.speaker.beep()

# Set motor to full speed for one second
motor.dc(100)
wait(1000)
motor.stop()

# Set motor to full negative speed for one second
motor.dc(-100)
wait(1000)
motor.stop()

# Using a counter run the motor from stop to full speed and back to stop
counter = 1

while counter < 100:

    motor.dc(counter)
    counter += 1
    wait(10)

while counter > 0:

    motor.dc(counter)
    counter -= 1
    wait(10)

motor.stop()

# Beep to end the program
ev3.speaker.beep()

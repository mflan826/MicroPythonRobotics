from machine import Pin
# get the config library for Pic
import time

led = Pin(25, Pin.OUT)
# create an object configured to the Pin with the Pico LED

# while loop for blinking the LED
while True:
    led(1)
    print("LED IS ON")
    time.sleep(1)
    led(0)
    print("LED IS OFF")
    time.sleep(1)

# While in REPL, use control c to turn the program off or control d to start


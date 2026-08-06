from machine import Pin
from time import sleep

green = Pin(2, Pin.OUT)
red = Pin(3,Pin.OUT)

green.on()
red.off()

sleep(5)
green.off()
red.on()

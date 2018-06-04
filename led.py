from gpiozero import LED
from time import sleep

led = LED(19)

def ledon():
    led.on()
    sleep(.5)
    led.off()

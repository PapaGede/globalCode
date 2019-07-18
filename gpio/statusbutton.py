from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)
status=True


while (status==True):
    button.when_pressed = led.on

while (status==True):
    button.when_pressed = led.off



pause()
import math
from gpiozero import PWMLED
from time import sleep
 
led = PWMLED(21)
 
# while True:
#      led.value = 0 #off
#      sleep(1)
#      led.value = 0.5 #half brightness
#      sleep(1)
#      led.value = 1 # full brightness
#      sleep(1)

LEDLVL = 10

for i in range(0,2)
    for j in range(0,4)
        led.value = math.sin((i/LEDLVL)*math.pi)
        sleep(1)
        j+=1
    led.value=math.sin(0)
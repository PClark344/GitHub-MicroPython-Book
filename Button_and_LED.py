import utime
import machine

time_delay_long = 3
time_delay_short = 1

button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
led_red = machine.Pin(15, machine.Pin.OUT)

while True:
    if button.value() == 1:
        print('button pressed')
        led_red.value(1)
        utime.sleep(time_delay_long)
    led_red.value(0)
    
    

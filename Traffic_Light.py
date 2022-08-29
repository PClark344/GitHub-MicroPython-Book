import utime
import machine

# constants
time_delay_long = 3
time_delay_short = 1

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(12, machine.Pin.OUT)

# main body
try:
    while True:
 
        led_red.value(1)
        utime.sleep(time_delay_long)
        led_amber.value(1)
        utime.sleep(time_delay_short)
        led_red.value(0)
        led_amber.value(0)
        led_green.value(1)
        utime.sleep(time_delay_long)
        led_green.value(0)
        led_amber.value(1)
        utime.sleep(time_delay_long)
        led_amber.value(0)

finally:
    print('finishing')
    led_red.value(0)
    led_amber.value(0)
    led_green.value(0)
    
    

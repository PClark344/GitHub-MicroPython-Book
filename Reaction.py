import utime
import machine
import urandom

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)

try:
    
    def button_handler(pin):
        global pressed
        if not pressed:
            pressed = True
            timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
            timer_reaction = abs(timer_reaction)
            timer_reaction = round(timer_reaction,3)
            print('Your reaction time was ' + str(timer_reaction) + ' milliseconds')
                  
            
    led.value(1)
    utime.sleep(urandom.uniform(2, 7))
    led.value(0)
    timer_start = utime.ticks_ms
    button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

finally:
    led.value(0)

    

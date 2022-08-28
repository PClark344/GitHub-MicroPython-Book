import utime
import machine
import _thread

time_delay_long = 3
time_delay_short = 1
time_delay_very_short = 0.01
buzzer_duration = 200

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(12, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer = machine.Pin(0,machine.Pin.OUT)

global button_pressed
button_pressed = False

try:
    
    def button_reader_thread():
        global button_pressed
        while True:
            if button.value() == 1:
                button_pressed = True
                print('button pressed')
            utime.sleep(time_delay_very_short)
           
    _thread.start_new_thread(button_reader_thread,())   

    while True:
        if button_pressed == True:
            led_red.value(1)
            for i in range(buzzer_duration):
                buzzer.value(1)
                utime.sleep(time_delay_very_short)
                buzzer.value(0)
                utime.sleep(time_delay_very_short)                
            global button_pressed
            button_pressed =  False
            
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
    buzzer.value(0)   
    

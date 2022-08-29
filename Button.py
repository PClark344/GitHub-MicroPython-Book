import utime
import machine

button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)

while True:
    print(button.value())
    utime.sleep(1)


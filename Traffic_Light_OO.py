import utime
import machine

# constants
time_delay_long = 1
time_delay_short = 1

led_red1 = machine.Pin(15, machine.Pin.OUT)
led_amber1 = machine.Pin(13, machine.Pin.OUT)
led_green1 = machine.Pin(12, machine.Pin.OUT)

led_red2 = machine.Pin(15, machine.Pin.OUT)
led_amber2 = machine.Pin(13, machine.Pin.OUT)
led_green2 = machine.Pin(12, machine.Pin.OUT)

# initialise

# classes
class TL():
    def __init__(self):
        self.rlist = [1,0,0]
        self.ralist = [1,1,0]
        self.glist = [0,0,1]
        self.alist = [0,1,0]

def tl_seq():
    tlight = TL()
    utime.sleep(time_delay_long)
    print(tlight.ralist)
    utime.sleep(time_delay_long)
    print(tlight.glist)
    utime.sleep(time_delay_long)
    print(tlight.alist)   
    utime.sleep(time_delay_long)
    print(tlight.rlist)

while True:
    for tl_cnt in range(5):
        print(tl_cnt)
        tl = tl_seq()

print('finishing')

    

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

RLIST = [1,0,0]
RALIST = [1,1,0]
ALIST = [0,1,0]
GLIST = [0,0,1]

# initialise

# classes
class TL():
    def __init__(self,RLIST,RALIST,ALIST,GLIST):
        self.rlist = RLIST
        self.ralist = RALIST
        self.glist = GLIST
        self.alist = ALIST

    def tl_seq():
        tlight = TL()
        print(tlight.rlist)
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
        tl = TL.tl_seq()

print('finishing')

    

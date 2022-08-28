import utime
import machine

# constants
time_delay_long = 3
time_delay_short = 1

# classes
class TL():
    def __init__(self):
        self.rlist = [1,0,0]
        self.ralist = [1,1,0]
        self.glist = [0,0,1]
        self.alist = [0,1,0]

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
   
for tl_cnt in range(2):
    while True:
        tl_seq()


print('finishing')

    

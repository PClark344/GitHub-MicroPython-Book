import utime
import machine

# classes
#class T_Lights(red,amber,green):
#    def __init__(self,red,amber,green):
#        self.red = red
#        self.amber = amber
#        self.green = green

#tlight = T_Lights(1,0,0)

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)


print('finishing')

    

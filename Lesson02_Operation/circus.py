def light_on():
    print("The light is ON")

def light_off():
    print("The light is OFF")
    
def juggeler():
    print("My name is Piter")
    print("I am juggling now")
    
def singer ():
    print("My name is Antonio Banderas")
    print("I am singing now")
    
def clown():
    print("My name is Julico Bandito")
    print("I am clowning now")
    
def entertainer():
    clown()
    singer()
    juggeler()
    
def circus():
    light_on()
    entertainer()
    light_off()
  
circus()
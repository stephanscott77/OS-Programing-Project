# Names:  Danielle Hemmings, 
#         Tyandra Taylor, 
#         Chadwick Hewitt, 
#         Stephan Scott, 
#         Kyle Parris (1804904)
#OS Programming Project

import datetime

inLine = []
outLine = []
doorIn = []
doorOut = []

class Customer:
  def __init__(cus, cusNum, arrivalTime, entryTime, shoppingTime, waitTime, exitTime):
    cus.cusNum = cusNum
    cus.arrivalTime = arrivalTime
    cus.entryTime = entryTime
    cus.shoppingTime = shoppingTime
    cus.waitTime = waitTime
    cus.exitTime = exitTime
    
  def __str__(cus):
    return f"{cus.cusNum} - {cus.arrivalTime} - {cus.entryTime} - {cus.shoppingTime} - {cus.waitTime} - {cus.exitTime}"
  
#cus1 = Customer(1, 2, 3, 4)
#print(cus1)
def generateCustomer():
  for x in range(55):
    time = datetime.datetime.now()
    cus = Customer(x, time, 0, 0, 0, 0)
    inLine[x] = cus
    wait()
    
class Door:
    def __init__(self):
        self.compartments = [None, None, None, None] # Initialize empty compartments

    def add_person(self, person):
        if None in self.compartments: # Check if there's an empty compartment
            index = self.compartments.index(None) # Find the index of the first empty compartment
            self.compartments[index] = person # Add person to the compartment
            print(f"{person} added to compartment {index+1}")
        else:
            print("Door is already full, cannot add person")

    def rotate(self):
        if self.compartments[-1] is not None: # Check if the last compartment is occupied
            print("Door is rotating...")
            self.compartments = [self.compartments[-1]] + self.compartments[:-1] # Rotate the compartments
        else:
            print("Cannot rotate door, last compartment is empty")

door = Door()
door.add_person("Alice")
door.add_person("Bob")
door.add_person("Charlie")
door.add_person("Dave")
door.add_person("Eve") # This will not be added, since the door is already full
door.rotate() # This will rotate the compartments



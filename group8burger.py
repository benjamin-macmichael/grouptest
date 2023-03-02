#Ben Macmichael, Mason Phelps, Dalan Cluff, Caden Baird, Chris Prinster, Caleb Brown
#Create a program to track exactly how many hamburgers each of our customers orders

import random

#create a class called Order for assigning burger count
class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()
        
        #create a method that pulls a random number between 1 and 20 for burger count
    def randomBurgers(self):
        iburgervalue = random.randint(1,20)
        return iburgervalue

#create a class called Person for assigning names to customers
class Person:
    def __init__(self):
        self.customer_name = self.randomName()

    #create a method with list of 9 names that returns a random name from the list
    def randomName(self):
        asCustomers = ["Jefe","El Guapo","Lucky Day","Ned Nederlander","Dusty Bottoms","Harry Flugleman","Carmen","Invisible Swordsman","Singing Bush"]
        name = random.choice(asCustomers)
        return name
    
#create a Customer class that inherits person attributes and has an order object as an attribute 
#so that every customer object has a name attribute and a burger count attribute
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

#create a queue
queueCustomers = []

#create a loop that fils the queue with 100 customers (objects)
iCount = 0
while iCount < 100 :
    queueCustomers.append(Customer())
    iCount += 1

#create the dictionary
dictCustomer = {}

#create a loop that takes the value in the first position of the queue and checks the dictionary for a key (which is the name)
#if the name is in the dictionary then increment the burger total, if not then create a new key and value in the dictionary.
#Loop through 100 times
iCnt = 0
while iCnt < 100 :
    if queueCustomers[0].customer_name in dictCustomer :
        dictCustomer[queueCustomers[0].customer_name] = dictCustomer[queueCustomers[0].customer_name] + queueCustomers[0].order.burger_count
    else:
        dictCustomer[queueCustomers[0].customer_name] = queueCustomers[0].order.burger_count
    #pop first value in queue so when it goes back through the loop it's the next customer
    queueCustomers.pop(0)
    iCnt += 1

#take keys and values from dictionary and sort them by burger count from greatest to least into a list
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True) 

print("\n")
#create a loop that prints the name and burger count for each customer in postion 0 of the list
for key, value in dictCustomer.items() :
    print((listSortedCustomers[0][0].ljust(19)) + "     " + str(listSortedCustomers[0][1]) + "\n")
    #pop position 0 so when it goes back through the loop it prints the next combo of customer name and burger count
    listSortedCustomers.pop(0)




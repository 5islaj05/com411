#Asks the user to give us a number to calculate factorial
User_Input = int(input("Please give us a number: "))

counter = 0 #controlled by the loop so it makes sure we dont loop further than what the user requires us to go
factorial = 1 #The factorial. calculated by multiplying the counter by itself

while ( counter < User_Input ):
    counter += 1
    factorial = factorial * counter  #Calcualtes factorial by multiplyig factorial by the counter (which loops until counter is equal to what the user asked.)

print("The factorial is {}".format(factorial)) #prints out what the factorial is after calculating it
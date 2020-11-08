#Program will count to the sum of 100
print("Calculating the sum of the first 100 numbers...")

# Control variable which controls how many time the program loops
iterations = 1

#total for the sum of 100
total = 0

while (iterations <= 100):
    total = total + iterations
    iterations += 1

#Prints out the variable total (which is the sum of the first 100 numbers)
print("...Done! The answer is", total) 
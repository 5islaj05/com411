#Asks how many numbers we are finding the sum of.
Sum_Amount = int(input("How many numbers should I sum up? \n"))

# Iteration is set to one so when the loop occurs its starting at "1" instead of using 0
iterations = 1

# the total of the sums being added.
total = 0

#loops till iteration is equal the number of sums the user told us we're doing.
while (iterations <= Sum_Amount):
    #Asks the user number they want to use for the sum
    print("Please enter number", iterations, "of", Sum_Amount, ":")
    number = int(input("\n"))
    #Adds the number to the total to be displayed as the sum
    total = total + number

    #lets the program know it looped once
    iterations += 1

# Display result (the sum)
print("The answer is", total)


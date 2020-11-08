User_Input = int(input("How many cables should i remove? ")) #asks user the amount of cables to be removed

iterations = 0 #sets up iteration counter
while (User_Input > iterations):
  print("Removed cable.") #announces cable being removed
  iterations += 1 #adds one to the iterations

  #keeps looping till iterations equals User_Input

# Ask user for number of cables
print("How many live cables should I avoid?")
cables_to_avoid = int(input())

# Declare a control variable
cables_avoided = 0

# Avoid cables
print()

while (cables_avoided < cables_to_avoid):
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print("Done!", cables_avoided, "cables avoided.")
#Ask how many steps we're going to take
far = int(input("How far are we from the cave? \n"))

for stepped in range(far, 0, -1): #Loops till the "counter" known as stepped reaches 0
    print(stepped, "steps remaining.") #prints out the remaining step

print("We have reached the cave!") #prints out that they reached the cave after loops ends
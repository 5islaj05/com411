#Beeps ask which route they take
print("Beep> What type of adventure should i go for?") 
#prints out the choices the user gets
print(""" \n               Choices \n
           short, long, scary or safe \n """ )
adventureType = input()

#Prints out the route the user takes based on what option they chose
if (adventureType == "scary" or adventureType == "Scary") or (adventureType == "short" or adventureType == "Short"):
  print("Entering the dark forest...")

elif (adventureType == "safe" or adventureType == "Safe") or (adventureType == "long" or adventureType == "Long"):
  print("Taking the safe route!")
#tells user they inputted wrong route
else:
  print ("Not sure which route to take.")




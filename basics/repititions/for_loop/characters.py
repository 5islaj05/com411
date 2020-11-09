#asks the user for the markings
marking = input("What strange markings do you see? \n ")

print("Identifying..\n") #lets the user know the markings are being identified

for i in range(0, len(marking), 1):
   #loops through the characters in the markings and individually print them out
    print("index", i, ":", marking[i])
git
print("Done !")
  
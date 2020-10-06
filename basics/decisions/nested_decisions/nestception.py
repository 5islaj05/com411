#This sets up the setting and allows the user to start the "game"
print("Finding beep's battery")
print("""Loading in...""")
print("Beep> where should i look?")
print("Choices: Bedroom | Bathroom | Lab ") #important for users to know what choices they have

PrimaryLocation = input() #where the user wants to first visit

#nested if statements for Bedroom
#Honsty i wonder why i  never asked the "input question" in input() until now :)
if (PrimaryLocation == "bedroom" or PrimaryLocation== "Bedroom"):
  print("Beep> Where should i look?")
  print("""     choices
          1) Under the bed
          2) drawers
          3) clothes """)
   #This is where the user chooses where they're looking in the bedroom     
  bedLook = input("select a number from 1 to 3: ")
  if (bedLook == "1"):
    print("Found some shoes but no battery")
  elif (bedLook == "2"):
    print("Found some mess but no battery")
  elif (bedLook == "3"):
    print("Found a £20 note but no battery")
  else: 
    print("Found some mess but no battery")

else:
  print("I do not know where that is but I will keep looking")

#nested if statements for Bathroom
if (PrimaryLocation == "bathroom" or PrimaryLocation== "Bathroom"):
  print("Beep> Where in the Bathroom should i look?")
  print(""" Choices 
              1) bathtub
              2) sink
              3) toilet              """)
  bathtubLook = input("select a number from 1 to 3: ")
  if (bathtubLook == "1"):
    print("Found a rubber duck but no battery")
  elif (bathtubLook == "2"):
    print("Found a wet surface but no battery")
  elif (bathtubLook == "3"):
     print("you decided not to stick your hand in there...")
  else: 
     print("Found a wet surface but no battery")



#nested if statements for Lab
if (PrimaryLocation == "lab" or PrimaryLocation== "Lab"):
  print("Beep> Where in the Lab should i look?")
  print(""" Choices 
              1) on the table
              2) storage room
              3) trash room             """)
  labLook = input("select a number from 1 to 3:")
  #runs once a user chooses one of the options
  if (labLook == "1"):
    print("Yes! I found my battery")
  elif (labLook == "2"):
    print("Found some tools but no battery")
  elif (labLook == "3"):
     print("found some mess but no battery")
  else: 
     print("Found some tools but no battery")
     

  
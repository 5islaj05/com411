#asks what type of cover they have
print("What type of cover does the book have?")
cover = input()

#If a user answers   hard cover this code will execute and end the script.
if (cover == "hard" or cover == "Hard"):
  print ("Books with hard covers can be more expensive!")

#if the user replies soft they're given another question to answer
if (cover == "soft" or cover == "Soft"):
  print("Is the book perfect-bound? Yes or No")
  bound = input()
  if (bound == "yes" or bound =="Yes"):
    print("Soft cover, perfect bound books are very popular!")
    #If no or another answer is given this will be sent to them.
  else: 
    print("Soft covers with coils or stiches are great for short books")

 #Whenever an invalid response is given it lets the users know
else:
  print("Invalid option! ")
  print("Please use one of the following inputs: soft | hard")




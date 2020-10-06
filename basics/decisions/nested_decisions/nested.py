print("What type of cover does the book have?")
cover = input()

if (cover == "hard" or cover == "Hard"):
  print ("Books with hard covers can be more expensive!")

if (cover == "soft" or cover == "Soft"):
  print("Is the book perfect-bound? Yes or No")
  bound = input()
  if (bound == "yes" or bound =="Yes"):
    print("Soft cover, perfect bound books are very popular!")
  else: 
    print("Soft covers with coils or stiches are great for short books")





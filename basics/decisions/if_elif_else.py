#asks the user the question
print("Towards which direction should I paint (up, down, left or right)")
#stores the user's input
userInput = input()
#Reacts to users input
if (userInput == "up" or userInput== "Up"):
  print("I am painting in the upward direction!")

elif (userInput == "down" or userInput == "Down"):
  print("I am painting in the downwards   direction!" )

elif (userInput == "left" or userInput == "Left"):
  print("I am painting in the left direction!" )

elif (userInput == "right" or userInput == "Right"):
  print("I am painting in the right direction!" )

else:
  print("Unrecognised response")

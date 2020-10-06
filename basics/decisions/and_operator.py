#Asks questions
print("What did I hear?")
hearInput = input()
print("What did i see?")
seeInput = input()

# looking for two specific answers so we use and here
if (hearInput == "grr" and seeInput == "two red eyes"):
  print("Theres is a scary creature. i should get out of here!")
  #if the user gives another response this is what we get
else:
  print("I am a little scared but i will continue!")
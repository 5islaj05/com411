import random as rnd #imports the random function
Min_Value = int(input("Please enter the minimum value: ")) #asks for the minimum number 
Max_Value = int(input("Please enter the Maximum value: ")) #asks for the maximum number

#generates the answer the program is going to ask for
Answer = rnd.randrange(Min_Value,Max_Value, 1)


while True: #using while True as its the the simplistic loop since you can "break loop" when the answer is found.
  User_Input = int(input("I am thinking of a number between {} and {}.  Can you guess what it is?  ".format(Min_Value,Max_Value))) #Asks the user to guess the answer

  if (User_Input > Answer):  #if the user's guess is too high then tell them its too high
    print("Your guess is too high!")
    
  elif (User_Input < Answer): #if the user's guess is too low then tell them that
    print("Your guess is too low")

  elif(User_Input == Answer): #if the user guessed the right answer then tell them they did it and end loop.
    print("Congratulations! You guessed my number!")
    break 
  

#asks the user for two numbers and stores them
print("Please enter the first number.")
firstNumber = int(input())
print("Please enter the second number")
secondNumber = int(input())

#Checks if the first number is smaller than the second numbe the user gave
if (firstNumber < secondNumber):
  print("The first number is the smallest")

#checks if the first number is bigger than the second number
elif (firstNumber > secondNumber):
  print("The second number is the smallest")

#checks if the first number and second number are equal
elif (firstNumber == secondNumber):
  print("Both are equal")
  
#prints out an error if something weird ever happens
else:
  print("Error")


#Asks and stores the 3 numbers that the user gives us
print("Please enter the first number")
firstNumber = int(input())
print("Please enter the second number")
secondNumber = int(input())
print("please enter the third number")
thirdNumber = int(input())

#Sets the counters to 0 and creats them
even = 0
odd = 0

# sees if the number is Even and adds to the score if it is an even number
if (firstNumber % 2 == 0):
  even += 1
#sees if the number is odd and adds to the score if it is an odd number
elif (firstNumber % 2 == 1):
  odd += 1

if (secondNumber % 2 == 0):
  even += 1

elif (secondNumber % 2 == 1):
  odd += 1

if (thirdNumber % 2 == 0):
  even += 1

elif (thirdNumber % 2 == 1):
  odd += 1

#announces the results
print("There were",odd," odd numbers and",even,"even numbers")
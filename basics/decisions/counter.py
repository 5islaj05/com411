print("Please enter the first number")
firstNumber = int(input())
print("Please enter the second number")
secondNumber = int(input())
print("please enter the third number")
thirdNumber = int(input())


even = 0
odd = 0

if (firstNumber % 2 == 0):
  even += 1

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

print("There were",odd," odd numbers and",even,"even numbers")
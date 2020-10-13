print("Program started")
standardCharacter = input("Please enter a standard character: ")

if len(standardCharacter) > 1:
  print("Error! Please only input a single character")

else:
  print("The ASCII code for {} is {}".format(standardCharacter,ord(standardCharacter)))
  print("Program ended!")
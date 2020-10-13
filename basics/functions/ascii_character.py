print("Program started!")
asciiCode = int(input("Please input an ASCII code: "))



if (abs(asciiCode) in range(32,126)):
  print("The character represented by the ASCII code {} is {}.".format(asciiCode,chr(asciiCode)))
else:

  print("Error: You have given us an unreadable assci code")
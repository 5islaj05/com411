#varables needed to help calculate bmi
name = input("What is your name human? ")
age = int(input("How old are you (in years)? "))
height = float(input("How tall are you (in meters)?"))
weight = int(input("How much do you weigh (in kilograms)?"))

#calculates and prints out your bmi which is rounded by 2 decimal points. while also repeating your information
print(name, "you are",age,"years old and your bmi is ",round(weight / (height **2),2))
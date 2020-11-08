User_Phrase = input("Please enter a phrase? \n ")

# Declare a control variable
bop = 0

while (bop < len(User_Phrase)):
    print("Bop ",end="") #used end to show to not create  new line when printing.
    #could have  a variable which is created by the loop used then print the value at the end of it.
    bop += 1
    
print("\n") #moves to next line when program is done
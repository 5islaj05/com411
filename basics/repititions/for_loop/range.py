#asks the user how much brightness they need
required = int(input("What level of brightness is required? "))


print("\n Adjusting brightness..\n")
#
for brightness in range(2, required + 1):
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)
    print("") #seperates the message after being printed
    
#when the loop is done print out that adjustments are complete 
print(" \n Adjustments complete!") 

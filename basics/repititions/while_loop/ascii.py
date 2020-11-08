Bars_Charging = int(input("How many bars should be charged? "))

# helps loop repeat until device is fully charged
bars_charged = 0

print(" ")

while (bars_charged < Bars_Charging):
    bars_charged += 1
    print(" \n Charging:", " █" * bars_charged) #creates the bars as the user wants them. the bars_charged mutliplies that singular bar
    
print("The battery is fully charged.")  # announces the device is fully charged       
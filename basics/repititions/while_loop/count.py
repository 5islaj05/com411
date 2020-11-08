Cables_Avoiding = int(input("How many live cables should I avoid "))

# the cables that we have avoided. goes up every loop
Avoided_cables = 0

print("\n") #cleans the GUI  a bit

while (Avoided_cables < Cables_Avoiding):
    print("Avoiding...", end="")
    Avoided_cables = Avoided_cables + 1
    print("Avoiding...Done!", Avoided_cables, "live cables avoided.")
    
    
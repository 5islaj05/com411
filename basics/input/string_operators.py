#variables to asks user how much of each option they want
lives = int(input("Please enter the number of lives: "))
 
energy = int(input("Please enter the energy level: "))

shield = int(input("Please enter the shield level: "))

print("health has been set.")
#generates  the energy, lives and shield
print("Lives:","♥" *lives)
print("energy:","♦" *energy)
print("shield:","♦" * shield)


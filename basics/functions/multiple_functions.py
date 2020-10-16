def display_ladder(steps): #function to visualise ladder
  for i in range(0,steps,1): #loops the amount of steps there is
    print(""" 
    | |
    ***
    | | """)

def create_ladder(): #function to ask user for how many steps are left
  steps = int(input("How many steps remain?: ")) #gets the users input
  display_ladder(steps) #throws user input into display_ladder function to create the ladder


create_ladder() #finally calls upon the create_ladder process when code is ran.
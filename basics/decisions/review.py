def run():
  print("Adventure program V1")
  character = input("Please choose your username: ")

  print("You're a robot named",character,"and you wake up in a strange enviroment. you have to locate an exit and figure out whats going on.")

  print("\n you looked to the left and notice theres two doors... one that leads to the the cafeteria and one that leads to the laboratory")

  Choice1 = input("Do you want to enter the laboratory (lab) or cafeteria (cafe): ")

  if (Choice1 == "laboratory" or Choice1 == "laboratory" or Choice1 == "lab"):
    print("You entered the laboratory, you see a bunch of robots of simillar design to you and wonder if maybe you was born here. ")
    print("you hear a weird noise... it originated from the corner of the room")
    Choice1_2 = input("Do you investigate the loud noise? Y/N ")

    if (Choice1_2 == "Y" or Choice1_2 == "y"):
      print("You investigate the weird noise which you recognise as a beeping sound and locate a terminal which is asking you to fill in data.")

      quiz1 = int(input("Please select the anomaly in this list: 2, 4 , 6 ,7 ,8 10, 12, 14: "))
      quiz2 = int(input("Input what X is, 10 + X = 25  "))

      if (quiz1 == 7 and quiz2 == 15):
        print("Completed Terminal tasks!")
        print("operator",character,"was last scene on island X")
        print("You finally locate the exit by checking the map and escape")
      else:
        print("you failed to open the console and all the data was wiped beyond recovery. you're stuck")
  elif (Choice1 == "cafeteria" or Choice1 == "Cafeteria" or Choice1 == "cafe"):
    print("You entered the cafeteria and the lights went off...")
    print("You saw a bunch of tools on the table and can only carry two of these items")
    print(""" items on table
            1) Knife
            2) flashlight """)
    ItemChoice = int(input("What item do you take? (1-2): "))
    if (ItemChoice == 1):
      print("You took the knife just in time as you was attacked from behind. You whirl around and stab the animal that tried attacking you")
      print("You follow the path the animal took before attacking you as you notice the direction the body came from and found an exit which you use.")
    elif (ItemChoice == 2):
      print("You pickup the flashlight and see a shadow behind you, you activate the flashlight which blinds that animal and use it.")
      print("You realise the animal must have come from somewhere and you use the flashlight to observe your surrounding and notice there is an exit hidden.")

    else:
      print("You did not pick anything thus when you was attacked you wasnt able to defend yourself")



run()
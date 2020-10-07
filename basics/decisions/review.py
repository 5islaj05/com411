print("Adventure program V1")
character = input("Please choose your username: ")

print("You're a robot named",character,"and you wake up in a strange enviroment. you have to locate an exit and figure out whats going on.")

print("\n you looked to the left and notice theres two doors... one that leads to the the cafeteria and one that leads to the laboratory")

Choice1 = input("Do you want to enter the laboratory or cafeteria")

if (Choice1 == "laboratory" or Choice1 == "laboratory"):
  print("You entered the laboratory, you see a bunch of robots of simillar design to you and wonder if maybe you was born here. ")
  print("you hear a weird noise... it originated from the corner of the room")
  Choice1_2 = input("Do you investigate the loud noise? Y/N")

  if (Choice1_2 == "Y" or Choice1_2 == "y"):
    print("You investigate the weird noise which you recognise as a beeping sound and locate a terminal which is asking you to fill in data.")

    quiz1 = input("Please select the anomaly in this list: 2, 4 , 6 ,7 ,8 10, 11, 12, 14: ")
    quiz2 = input("Input what X is, 10 + X = 25")

    if (quiz1 == 11 and quiz2 == 15):
      print("Completed Terminal tasks!")
      print("operator",character,"was last scene on island X")

  if (Choice1 == "cafeteria" or Choice1 == "Cafeteria"):
    print("You entered the cafeteria and the lights went off...")
    print("You saw a bunch of tools on the table and can only carry two of these items")
    print(""" items on table
            1) Knife
            2) flashlight 

                              
                               """)



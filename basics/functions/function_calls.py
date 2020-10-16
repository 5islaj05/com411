#user input to lowercase function
def lower_case(user_inputted_word): 
  print(user_inputted_word.lower())
  
# user input to uppercase function
def upper_case(user_inputted_word):
  print(user_inputted_word.upper())
    
#displays a box around the users input function
def  display_box(user_inputted_word):
  box = 4 + len(user_inputted_word)
  print ("#" * box)
  print("# {} #".format(user_inputted_word))
  print("#" * box)
   
#displays user input in reverse
def mirrored_word(user_inputted_word):
  mirrored_word = ""
  for character in reversed(user_inputted_word):
    mirrored_word += character
  print(user_inputted_word, "|", mirrored_word )

  #repeats user's input but alternating between upper and lowercase 
def repeat(user_inputted_word):
  repeat_input= int(input(("how many times do you want the word to repeat? ")))

  for i in range(0,repeat_input,1):
    if (i % 2 == 0):
      upper_case(user_inputted_word)

    else:
      lower_case(user_inputted_word)



#asks for the user's inputted word and what option they'd like to run
def run():
  user_inputted_word = input("please input a word: ")
  print("""
  1) Display in a Box 
  2) Display Lower-case
  3) Display Upper-case 
  4) Display Mirrored 
  5) Repeat.
  6) nothing
  """)
  user_input = int(input("What would you like to do with the word? [1-6"))

  #runs the functions above according to the users input
  if user_input == 1:
    display_box(user_inputted_word)
  elif user_input == 2:
    lower_case(user_inputted_word)
  elif user_input == 3:
    upper_case(user_inputted_word)
  elif user_input == 4:
    mirrored_word(user_inputted_word)
  elif user_input == 5:
    repeat(user_inputted_word)
  elif user_input == 6:
    quit # stops the  program

  else:
    print("invalid option")
    
run() #when python file is ran this will make the program run



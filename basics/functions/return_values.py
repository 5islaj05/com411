def sum_weights(beep_weight,bop_weight):
  return beep_weight + bop_weight #returns the sum of the two parameters

def calc_avg_weight(beep_weight,bop_weight):
  return (beep_weight + bop_weight) /2 #returns the average of the two parameters

def run(): #run function to run all of the code
  #asks the user for the bot's weight
  beep_weight = int(input("what's beep's weight? "))
  bop_weight  = int(input("What's bop's weight? "))
  #ask user if they want to get the sum or average
  user_input = input("Do you want to calculate the sum or average?")

  #if it's sum then calculate the sum
  if (user_input == "sum" or user_input == "Sum"):
    print(sum_weights(beep_weight,bop_weight))
  #if it's average then calculate the average
  elif (user_input == "average" or user_input == "Average"):
    print(calc_avg_weight(beep_weight,bop_weight))
  #if an invalid option is chosen return this
  else:
    print("invalid option", user_input)


run() #runs the function run which utilises all the other functions

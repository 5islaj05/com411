def climb_ladder(stepsTaken,stepsRemaining): #creates a function
  if (stepsRemaining > stepsTaken): # if steps remaining is greater than steps taken it means you're almost done
    print("Still some way to go!")
  else:
    print("We're almost there")

climb_ladder(5, 2)  #returns the "almost there" value
climb_ladder(2, 5) #returns "still some way to go" value

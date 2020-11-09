#asks the user how many times they want the mountain to be displayd
display = int(input("How many mountains do you want?  "))
print("Displaying",display,"mountains...") #lets the user know how many mountains is going to be shown

for i in range(display): #loops the code in here the amount of times the user asked for above.
#print out the mountain
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\
     """) 
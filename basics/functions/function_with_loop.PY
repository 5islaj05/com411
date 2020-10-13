def escape_by(plan):

  if (plan == "jumping over"):
    print("We cannot escape that way! The boulder is too big")
    print()

  elif (plan == "running around"):
    print("We cannot escape that way! The boulder is too fast!")
    print()
  elif (plan == "going deeper"):
    print("That might just work! Let's go deeper!")
    print()
  else:
    print("We cannot that way! The boulder is in the way!")
    print()

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("going forward")

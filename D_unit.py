def unit_chooser():
  # defining the units possible
  units = ["mm", "cm", "m"]
  # while loop as error prevention
  valid = False
  while not valid:
    try:
      # ask user what unit they are using
      print("What is the unit that you are working in? mm/cm/m")
      user_unit = input().lower().strip()
      # check to see if user input is a valid input
      units.index(user_unit)
      print()
      #return the user input if the input is valid
      return user_unit
    except ValueError:
      # error message if user input is invalid
      print()
      print("Please enter one of the following units mm, cm, m")
      print()

for i in range(3):
  penis = unit_chooser()
def unit_chooser():
  units = ["mm", "cm", "m"]
  valid = False
  while not valid:
    try:
      print("What is the unit that you are working in? mm/cm/m")
      user_unit = input().lower().strip()
      units.index(user_unit)
      return user_unit
    except ValueError:
      print("Please enter one of the following units mm, cm, m")
      print()

penis = unit_chooser()
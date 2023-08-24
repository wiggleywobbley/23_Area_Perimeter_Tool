def shape_area():
  #listing variables
  shapes = ["circle", "square", "rectangle", "triangle", "parallelogram"]
  calcs = ["area", "perimeter"]
  error = ["Please enter one of the listed shapes", "Please enter either area or perimeter"]
  shape_area = []

  #error prevention to detect for a value error
  valid = False
  while not valid:
    try:
      #asking question
      print("What Shape do you want the area/perimeter calculated?")
      print("Circle, Square, Rectangle, Triangle, Parallelogram")
      shape = input().strip().lower()
      #if the user inputs something that is not on the list a value error will occur, causing         
      #the program to ask the same question again
      shapes.index(shape)
      shape_area.append(shape)
      valid = True
    except ValueError:
      #if triggered will display the appropriate error message from the list
      print()
      print(error[0])
      print()
  print()
  
  #error prevention to detect for a value error
  valid = False
  while not valid:
    try:
      #asking question
      print("Would you like to calculate the area or perimeter of this shape?")
      area_per = input().strip().lower()
      #if the user inputs something that is not on the list a value error will occur, causing         
      #the program to ask the same question again
      calcs.index(area_per)
      shape_area.append(area_per)
      valid = True
    except ValueError:
      #if triggered will display the appropriate error message from the list
      print()
      print(error[1])
      print()
  #return a list with the values for the shape and the calculation the user wants done
  print()
  return shape_area


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

      
def perimeter(shape):
  # state variable for the values to be stored
  dimensions = []
  # give each shape a value based on how many sides are needed to calculate area
  if shape == "triangle":
    shape_value = 4
  elif shape == "square":
    shape_value = 2
  else:
    shape_value = 5

  # put the shape value at in the list for unpacking in the dimension function
  dimensions.append(shape_value)
  for i in range(1, shape_value):
      # ask user the size of each side
      print(f"What is the size of side {i} (Don't include units):")
      side = int(input())
      print()
      # add each side to the list and return the list
      dimensions.append(side)
  return dimensions


def dimension(shape, calc):
  dimensions = []
  # see what calculations the user wants done
  if calc == "area":
    # see what shape the user wants the area calculated for
    if shape == "circle":
      # ask for the radius of the users circle
      print(f"What is the radius of your {shape} (Don't include units):")
      radius = int(input())
      dimensions.append(radius)
      print()
    elif shape == "square":
      print(f"What is the size of 1 side of your {shape} (Don't include units):")
      side_size = int(input())
      dimensions.append(side_size)
      print()
    else:
      print(f"What is the height of your {shape} (Don't include units):")
      height = int(input())
      dimensions.append(height)
      print()
      print(f"What is the width of your {shape} (Don't include units):")
      width = int(input())
      dimensions.append(width)
      print()
  else:
    # see what shape the user wants the perimeter calculated for
    if shape == "circle":
      # ask for the radius of the users circle
      print(f"What is the radius of your {shape} (Don't include units):")
      radius = int(input())
      dimensions.append(radius)
      print()
    else:
      # call on the perimeter function
      lengths = perimeter(shape)
      # unpack the users inputs from the perimeter function
      for i in range(1, lengths[0]):
        add_lengths = lengths[i]
        dimensions.append(add_lengths)

  # return the user inputs
  return dimensions


def calculate(calcs, shape, dimensions):
  # see if the user wants to calculate the area or perimeter
  if calcs == "area":
    # see what shape the user has to make sure that we are using the right formula
    if shape == "triangle":
      answer = (dimensions[0] * dimensions[1]) * 0.5
    elif shape == "circle":
      answer = 3.14 * (dimensions[0] ** 2)
    elif shape == "square":
      answer = dimensions[0] ** 2
    else:
      answer = dimensions[0] * dimensions[1]
  else:
    if shape == "triangle":
      answer = dimensions[0] + dimensions[1] + dimensions[2]
    elif shape == "circle":
      answer = (dimensions[0] * 2) * 3.14
    elif shape == "square":
      answer = dimensions[0] * 4
    else:
      answer = dimensions[0] + dimensions[1] + dimensions[2] + dimensions[3]

  # return the area/perimeter to be printed and presented to the user
  return answer

for i in range(2):
  # run the function shape_area to find out what calculations the user wants to make for what shape
  shape_and_area = shape_area()
  
  # run the function unit_chooser to see what unit the user is working with
  user_unit = unit_chooser()
  
  # while loop to have error correction and a maximum number for the dimension function
  valid = False
  while not valid:
    try:
      # run the function dimension with the 2 outputs from shape_area 
      dimensions = dimension(shape_and_area[0], shape_and_area[1])
      # find how long the dimensions list is
      value_lenth = len(dimensions)
      # for loop to check each value in the list to make sure the value is a number that is below 50
      for i in range(value_lenth):
        value = dimensions[i]
        int(value)
        if value > 50:
          int("Force ValueError")
        valid = True
    except ValueError:
      # print error message if an error occurs during the dimension function
      print("Please enter number symbols that are below 50")
      print()
      valid = False
  
  # put the values collected from the dimension function into a calculator to find the area/perimeter
  answer = calculate(shape_and_area[1], shape_and_area[0], dimensions)
  
  # define what the final statement will be
  final_statment = f"The {shape_and_area[1]} of your {shape_and_area[0]} is {answer}{user_unit}"
  
  if shape_and_area[1] == "area":
    # if the user wants area calculated have the final unit be displayed as units squared
    print(final_statment + "²")
  elif shape_and_area[1] == "perimeter" and shape_and_area[0] == "circle":
    # if the user wanted the perimeter of a circle calculated make sure the final statment says circumference
    print(f"The circumference of your {shape_and_area[0]} is {answer}{user_unit}")
  else:
    print(final_statment)
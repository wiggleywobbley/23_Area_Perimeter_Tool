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
      print(error[0])

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
      print(error[1])
  #return a list with the values for the shape and the calculation the user wants done
  return shape_area

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

def perimeter(shape):
  dimensions = []
  if shape == "triangle":
    shape_value = 4
  elif shape == "square":
    shape_value = 2
  else:
    shape_value = 5

  dimensions.append(shape_value)
  for i in range(1, shape_value):
      print(f"What is the size of side {i} (Don't include units):")
      side = int(input())
      dimensions.append(side)
  return dimensions


def dimension(shape, calc):
  dimensions = []
  if calc == "area":
    if shape == "circle":
      print(f"What is the radius of your {shape}:")
      radius = int(input())
      dimensions.append(radius)
    else:
      print(f"What is the height of your {shape}:")
      height = int(input())
      dimensions.append(height)
      print()
      print(f"What is the width of your {shape}:")
      width = int(input())
      dimensions.append(width)
  else:
    if shape == "circle":
      print(f"What is the radius of your {shape}:")
      radius = int(input())
      dimensions.append(radius)
    else:
      lengths = perimeter(shape)
      for i in range(1, lengths[0]):
        add_lengths = lengths[i]
        dimensions.append(add_lengths)

  return dimensions


def calculate(calcs, shape, dimensions):
  # see if the user wants to calculate the area or perimeter
  if calcs == "area":
    # see what shape the user has to make sure that we are using the right formula
    if shape == "triangle":
      answer = (dimensions[0] * dimensions[1]) * 0.5
    elif shape == "circle":
      answer = 3.14 * (dimensions[0] ** 2)
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


shape_area = shape_area()

user_unit = unit_chooser()

valid = False
while not valid:
  try:
    dimensions = dimension(shape_area[0], shape_area[1])
    value_lenth = len(dimensions)
    for i in range(value_lenth):
      value = dimensions[i]
      int(value)
      if value > 50:
        int("Force ValueError")
      valid = True
  except ValueError:
    print("Please enter numbers that are below 50")
    valid = False

answer = calculate(shape_area[1], shape_area[0], dimensions)

print(f"The {shape_area[1]} of your {shape_area[0]} is {answer}{user_unit}")
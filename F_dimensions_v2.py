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
      print(f"What is the radius of your {shape}:")
      radius = int(input())
      dimensions.append(radius)
      print()
    elif shape == "square":
      print(f"What is the size of 1 side of you {shape}:")
      side_size = int(input())
      dimensions.append(side_size)
      print()
    else:
      print(f"What is the height of your {shape}:")
      height = int(input())
      dimensions.append(height)
      print()
      print(f"What is the width of your {shape}:")
      width = int(input())
      dimensions.append(width)
      print()
  else:
    # see what shape the user wants the perimeter calculated for
    if shape == "circle":
      # ask for the radius of the users circle
      print(f"What is the radius of your {shape}:")
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
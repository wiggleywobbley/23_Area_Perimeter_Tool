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

def dimensions(shape, calc):
  input = 0
  valid = False
  while not valid:
    try:
      dimensions = []
      if calc == "area":
        if shape == "circle":
          print(f"What is the radius of your {shape}:")
          input = int(input())
          dimensions.append(input)
        else:
          print(f"What is the height of your {shape}:")
          input = int(input())
          dimensions.append(input)
          print()
          print(f"What is the width of your {shape}:")
          input = int(input())
          dimensions.append(input)
      else:
        if shape == "circle":
          print(f"What is the radius of your {shape}:")
          input = int(input())
          dimensions.append(input)
        else:
          lengths = perimeter(shape)
          for i in range(1, lengths[0]):
            dimensions.append(i)
    except ValueError:
      print("Please enter a number that is bellow 50")

  return dimensions

penis = dimensions("rectangle", "perimeter")
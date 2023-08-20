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
        dimensions.append(i)

  return dimensions

for i in range(10):
  dumb = input("area or perimeter? ")
  cunt = input("what shape? ")
  bitch = dimensions(cunt, dumb)

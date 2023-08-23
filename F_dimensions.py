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
        add_lengths = lengths[i]
        dimensions.append(add_lengths)

  return dimensions


valid = False
while not valid:
  try:
    cum = dimensions("triangle", "perimeter")
    value_lenth = len(cum)
    for i in range(value_lenth):
      value = cum[i]
      if value > 50:
        int("Force ValueError")
      int(value)
      valid = True
  except ValueError:
    print("Please enter numbers that are below 50")
    valid = False
    
print(cum)

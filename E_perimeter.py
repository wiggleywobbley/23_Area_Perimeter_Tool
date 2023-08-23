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
def perimeter(shape):
  dimensions = []
  if shape == "triangle":
    shape_value = 4
  elif shape == "square":
    shape_value = 2
  else:
    shape_value = 5
    
  for i in range(1, shape_value):
    valid = False
    while not valid:
      try:
        print(f"What is the size of side {i} (Don't include units):")
        side = float(input())
        dimensions.append(side)
        valid = True
      except ValueError:
        print("Please enter a number:")
  return dimensions

for i in range(4):
  cunt = input("What shape do you want to know the perimeter for? ")
  bitch = perimeter(cunt)
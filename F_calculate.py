def calculate(calcs, shape, dimensions):
  if calcs == "area":
    if shape == "triangle":
      answer = (dimensions[0] * dimensions[1]) * 0.5
    elif shape == "circle":
      answer = 3.14 * (dimensions[0] ** 2)
    else:
      answer = dimensions[0] * dimensions[1]
  else:
    if shape == "triangle":
      answer = dimensions[0] + dimensions[1], dimensions[2]
    elif shape == "circle":
      answer = (dimensions[0] * 2) * 3.14
    else:
      answer = dimensions[0] + dimensions[1], dimensions[2] * dimensions[3]

  return answer
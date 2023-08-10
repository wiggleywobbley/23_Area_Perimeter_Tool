def shape_area():
  shapes = ["circle", "square", "rectangle", "triangle", "parellelogram"]
  error = "You must enter one of the listed shapes"
  shape_area = []
  
  valid = False
  while not valid:
    try:
      print("What Shape do you want the area/perimeter calculated?")
      print("Circle, Square, Rectangle, Triangle, Parellelogram")
      shape = input().strip().lower()

      shapes.index(shape)
      shape_area.append(shape)
      valid = True
    except ValueError:
      print(error)



  
  return shape_area
penis = shape_area()
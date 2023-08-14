def shape_area():
  #listing variables
  shapes = ["circle", "square", "rectangle", "triangle", "parellelogram"]
  calcs = ["area", "perimeter"]
  error = ["Please enter one of the listed shapes", "Please enter either area or perimeter"]
  shape_area = []

  #error prevention to detect for a value error
  valid = False
  while not valid:
    try:
      #asking question
      print("What Shape do you want the area/perimeter calculated?")
      print("Circle, Square, Rectangle, Triangle, Parellelogram")
      shape = input().strip().lower()
      #if the user inputs something that is not on the list a value error will occur, causing         the program to ask the same question again
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
      #if the user inputs something that is not on the list a value error will occur, causing         the program to ask the same question again
      calcs.index(area_per)
      shape_area.append(area_per)
      valid = True
    except ValueError:
      #if triggered will display the appropriate error message from the list
      print(error[1])
  #return a list with the values for the shape and the calculation the user wants done
  return shape_area

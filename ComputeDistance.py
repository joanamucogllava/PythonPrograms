# This program will compute the distance between two points
# that user will provide.

x1, y1 = eval(input("Enter x1 and y1 for Point1: "))
x2, y2 = eval(input("Enter x2 and y2 for Point2: "))
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print("The distance between the two points is", distance)

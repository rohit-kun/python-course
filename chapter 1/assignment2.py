# question - take diameter as input and calculate the area of a circle

diameter = int(input("Enter the diameter: "))
radius = diameter/2
area = 3.14 * (radius ** 2)
print(f"Area of circle: {area}")
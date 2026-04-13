pi = 3.14  

def areaOfCircle(radius):
    return pi * radius * radius


radius = float(input("Enter the radius of the circle: "))
area = areaOfCircle(radius)


print("The area of the circle is:" , area)


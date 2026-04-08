infinite = 1
total_miles = 0
total_gallons = 0

while infinite == 1:
    gallons = float(input("Enter gallons used (-1 to end): "))
    if gallons == -1:
        break

    miles = float(input("Enter miles driven: "))
    milesPerGallon = miles / gallons

    print(f"Miles per gallon for this tank was {milesPerGallon:.3f}")

    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    total_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was {total_mpg:.5f}")
else:
    print("No data entered.") 
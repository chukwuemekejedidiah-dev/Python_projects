Score = int(input("Enter your Score:"))

if Score > 100:
   print("Enter a score between 0 and 100")

elif Score >= 70 and Score < 101:
   print("You got an A")

elif Score >= 60 and Score < 70:
   print("You got a B")

elif Score >= 50 and Score < 60:
   print("You got a C")

elif Score >= 45 and Score < 50:
   print("You got a D")

else:
   print("You failed")
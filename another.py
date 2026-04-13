firstNum = int( input("Enter a number: "))
secondNum = int( input("Enter a number: "))

if (firstNum * 3) % (secondNum * 2) == 0:
  print("the first number tripled is a multiple of the second number doubled")
else:
  print("No it is not correct")  
# items = ("v", "i", "v", "i", "a", "n")
#
# letter = input("Enter a letter to check if it is in items: ")
#
# def check_item(item):
#     if item in items:
#         print(f"{item} is in this tuple")
#     else:
#         print(f" Element {item} does not exist inside this tuple.")
#
# check_item(letter)


# append a list with the "+=" operator

# a_list = []
# for i in range(1,6):
#     a_list += [i]
# print(a_list)

# letters = []
# letters += 'Python'
# print(letters)


# looping through a tuple

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def cube_list(values):
#     for i in range(len(values)):
#         values[i] = values[i] ** 3
#
# cube_list(numbers)
# print(numbers)t

# unpacking a tuple

# numbers = 1,2,3
# a,b,c = numbers
# print(a)
# print(b)
# print(c)



# converting a tuple to a list and back to add values to the tuple

# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# my_list.append(4)
#
# my_tuple = tuple(my_list)
# print(my_tuple)



# slices
#[start:stop:step]

# unpacking a tuple

#1
# student_tuple = ('Amanda',[98,85,87])
# first_name,grades = student_tuple
# print(first_name)
# print(grades)

#2
# number = (1, 2, 3, 4)
# number1, number2, number3, number4 = number
# print(number1, number2, number3, number4)


# using the del key word to remove elements form a list
# numbers = (list(range(0,10)))
# del numbers[0:2]
# print(numbers)


# sorting lists
#numbers = [10,6,7,8,6,4,2,1,3,]
#numbers.sort() # the sort function sorts it in ascending order 
#print(numbers)
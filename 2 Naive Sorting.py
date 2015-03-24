'''list_of_numbers = []

number_1 = int(input("Enter first number"))
list_of_numbers.append(number_1)
number_2 = int(input("Enter second number"))
list_of_numbers.append(number_2)
number_3 = int(input("Enter third number"))
list_of_numbers.append(number_3)
'''

list_of_numbers = input("type in 3 numbers with a space in between each >>>")
list_of_numbers=list_of_numbers.split(' ')

list_of_numbers.sort()

print (list_of_numbers)

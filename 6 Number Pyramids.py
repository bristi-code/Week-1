'''6 Number pyramids
 Write a program that takes an integer and outputs a number pyramid like the one below up to that integer (in example, 7 has been entered).
1 
22 
333 
4444 
55555 
666666 
7777777 
'''

input_number = int(input("Insert number here"))

for input_number in range (1, input_number+1): 
    print (str(input_number)*input_number)


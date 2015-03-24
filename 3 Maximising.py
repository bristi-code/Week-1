'''3 Maximising 
Write a program that read an (arbitrarily long) sequence of positive numbers.
The sequence is ended when the users enters “-1”.
At that point, the program must output the highest number in the sequence.
'''


number_sequence = []
input_number=0 #predefine a value so that number can be compared on next line
while input_number != -1:
    input_number = int(input ("Enter number now"))
    number_sequence.append (input_number)

    

print (max(number_sequence))


'''4 Going up! 
Read an arbitrarily long sequence of positive numbers from the user, until -1 is entered. 
At that point, print ”Yes” if the numbers were consecutive and increasing and ”No” otherwise.
Sequences ”1,2,3,4,-1” and ”5,6,7,8,9,10,11,-1” should output ”Yes”, but ”2,3,5,6,7,-1”, ”10,9,8,7,-1”, and ”1,1,2,3,4,5,-1” should output ”No”.
'''


number_sequence = []
valid = True
input_number=0 #predefine a value so that number can be compared on next line
while input_number != -1:
    input_number = int(input ("Enter number now"))
    if len(number_sequence) > 0 and input_number != -1:
        prev_number = number_sequence[len(number_sequence)-1]
        if prev_number != input_number-1:
                valid=False
    number_sequence.append (input_number)

if len(number_sequence)==1 :
    valid=False

if valid == True: print ("Yes")
else: print ("No")

'''5 You said high, I said low. . . 
Modify your former program so that it outputs ”Yes” when the numbers are consecutive, regardless of whether they go up or down.
For example, both ”2,3,4,5,6,-1” and ”10,9,8,7,-1” should now result in ”Yes”.
'''


number_sequence = []
valid = True
currDifference = 0
input_number=0 #predefine a value so that number can be compared on next line
while input_number != -1:
    input_number = int(input ("Enter number now"))
    if len(number_sequence) == 2 and input_number != -1:
            if currDifference==0 :
                currDifference = number_sequence[1] - number_sequence[0]
            else:
                if (number_sequence[1] - number_sequence[0])!= currDifference:
                    valid = False
                    
    
    number_sequence.append (input_number)

if len(number_sequence)==1 :
    valid=False

print (valid)

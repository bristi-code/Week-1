

# Ask user to input number
#n = input("Input number")

def is_prime(n):
    i = 2
    if n < 2:
        return False
    
    while i < n:        
        if n % i == 0:
            return False
        else:
            i += 1
    return True

test_number = int(input("Input number"))

print (is_prime(test_number))

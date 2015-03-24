'''10 No Consonants
Write a program that takes a string literal and returns the same string with all of the consonants removed.
'''

def remove_consonants(text):

    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')

    for char in text:

        if char  not in vowels:

            text = text.replace(char, '')

    return text

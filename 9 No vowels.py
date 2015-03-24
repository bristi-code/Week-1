'''9 No Vowels
Write a program that takes a string literal and returns the same string with all of the vowels removed

HINT: This should NOT use the input() or print() functions. It should be called by manually typing in a string (e.g. function(“this is a string”)) and you shoulds test that it works by returning the function to the print function.
'''

def remove_vowels(text):

    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')

    for char in text:

        if char in vowels:

            text = text.replace(char, '')

    return text

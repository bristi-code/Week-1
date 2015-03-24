def reverse(text):
    reversed_text = ""   

    for n in range(len(text)):
        reversed_text += text[-1 - n]
# so with each iteration the new reversed_text = reversed_text + whatever bit of the original text string 

# Capitalise the first letter, alternatively can use the .title() which capitalises first letter of every word
    return reversed_text.upper(0)



letter = input("Press a letter: ")
if letter.islower():
    letter = letter.upper()
elif letter.isupper():
    letter = letter.lower()

print(letter)
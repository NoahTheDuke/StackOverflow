# Selected as winner!
array = []

def guess_function():
    guess = input("Enter a letter:  ")
    guess = guess.upper()
    while ord(guess) < 64 or ord(guess) > 90:
        print("Invalid input, please try again..")
        guess = input("Enter a letter: ")
        guess = guess.upper()
    return guess

def populate_array(array):
    while len(array) < 26:
        guess = guess_function()
        array.append(guess)
        print(array)

print(populate_array(array))

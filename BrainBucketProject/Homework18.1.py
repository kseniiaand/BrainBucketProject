import random
guessestaken = 0

print("Hello! What's your name?\n")
name = input()

number = random.randint(0, 50)
print("Well, "+name+ ", I am thinking of a number between 0 and 50 ")

for guessestaken in range(7):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("The value is too low")

    if guess > number:
        print("The value is too high")

    if guess == number:
        break
if guess == number:
    guessestaken = str(guessestaken + 1)
    print("You guessed correctly")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was "+number+".")
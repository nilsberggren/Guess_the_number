import random

number = random.randint(1, 101)
guess = 0

# print(number)
print("The number is a number between 1 and 100.")


while int(guess) != number:
    guess = input("Guess the number: ")
    if int(guess) > number:
        print("Your guess were too high, try a lower number.")

    if int(guess) < number:
        print("Your guess were too low, try a higher number.")

if int(guess) is number:
    print(f"You were right, the number is {guess}.")

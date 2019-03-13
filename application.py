import random

number = random.randint(1, 101)
guess = 0
rounds = 0
max_rounds = 10

#print(number)
print("The number is a number between 1 and 100. You have 10 tries to guess the number. Good luck!")


while int(guess) != number:
    invalid_input = False
    if rounds is max_rounds:
        print("Game over man, you used all your tries.")
        break
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("That's not a number silly goose. Try again.")
        invalid_input = True

    if int(guess) not in range(1, 101) and not invalid_input:
        print("That's not in range, type a number from 1 to 100.")
    elif int(guess) > number and range(1, 101) and not invalid_input:
        rounds = rounds + 1
        print(f"Too high. You have {max_rounds - rounds} tries left.")
    elif int(guess) < number and range(1, 101) and not invalid_input:
        rounds = rounds + 1
        print(f"Too low. You have {max_rounds - rounds} tries left.")

if int(guess) is number:
    print(f"You were right, the number is {guess}.")

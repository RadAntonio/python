import random


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        print(f"You have 10 attempts remaining to guess the number")
        return 10
    elif difficulty == "hard":
        print(f"You have 5 attempts remaining to guess the number")
        return 5
    else:
        print("Sorry, I didn't understand that. Try again!")
        return choose_difficulty()


print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

number_of_guesses = choose_difficulty()
end_of_game = False
while not end_of_game:
    if number_of_guesses == 1:
        end_of_game = True
    guess = int(input("Guess: "))
    if guess == secret_number:
        print(f"You guessed the number in {number_of_guesses} guesses!")
    elif guess < secret_number:
        print("Your guess is too low.")
        number_of_guesses -= 1
    elif guess > secret_number:
        print("Your guess is too high.")
        number_of_guesses -= 1
    print(f"You have {number_of_guesses} guesses left.")

print(f"The number was {secret_number}.")




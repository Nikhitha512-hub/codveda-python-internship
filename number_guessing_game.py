import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Maximum attempts allowed
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have", max_attempts, "attempts.")

# Loop for attempts
for attempt in range(1, max_attempts + 1):

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    print("Attempts left:", max_attempts - attempt)

# If all attempts are used
if guess != secret_number:
    print("Game Over!")
    print("The correct number was:", secret_number)
import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"\nGuess a number between 1 and {x}: "))
        print("Your Guess Was: ", guess)
        if guess < randomNumber:
            print("Too Low")
        elif guess > randomNumber:
            print("Too High")
    print("\nYou Won")


def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    print("Choose a number between 1 and 1000, keep it to yourself")
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low         # Could also be high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed your number {guess}")


computerGuess(1000)
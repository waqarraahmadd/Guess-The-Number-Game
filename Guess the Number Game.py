from art import logo
import random

def difficulty():
    ask = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if ask == "easy":
        return EASY_TURNS 
    elif ask == "hard":
        return HARD_TURNS


def check_score(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1 
    elif guess < answer:
        print("Too low")
        return turns - 1 
    elif guess == answer:
        return f"You got it! You guessed the correct number: {answer}"


answer = random.randint(0,101)

EASY_TURNS = 10
HARD_TURNS = 5

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    print(f"Psst, the correct answer is {answer}")



    turns = difficulty()
    
    guess = 0 
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_score(guess, answer, turns)
        if turns == 0:
            print(f"You ran out of guesses, you lose. The answer was {answer}")
            return
game()
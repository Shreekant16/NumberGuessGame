hard = 5
easy = 10
import random


def set_difficulty():
    a = input("Enter hard or easy : ")
    if a.lower() == 'hard':
        return hard
    elif a.lower() == 'easy':
        return easy


def check(guess, correct, turn):
    if guess > correct:
        print("Too high")
        return turn - 1
    elif guess < correct:
        print("Too Low")
        return turn - 1


turn = set_difficulty()
number = random.randint(0, 100)
end = False
while not end:
    guess = int(input("Guess the number : "))
    turn = check(guess, number, turn)
    if turn == 0:
        print("You are out of lives.")
        end = True
    elif guess == number:
        print("you got it")
        end = True

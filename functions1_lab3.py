import random
def Guess():
    name = input("Hello! What is your name? \n")
    guess= int(input(f"\nWell, {name}, I am thinking of a number between 1 and 20. \nTake a guess. \n"))
    num = random.randint(1,20)
    cnt = 1
    while(cnt <= 20):
        if(guess > num):
            guess = int(input("\nYour guess is too high. \nTake a guess. \n"))
            cnt += 1
        elif guess < num:
            guess = int(input("\nYour guess is too low. \nTake a guess. \n"))
            cnt += 1
        elif guess == num:
            print(f"\nGood job, {name}! You guessed my number in {cnt} guesses! ")
            break
Guess()
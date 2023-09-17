"""
pick a random number game
"""
import random
n = random.randrange(1,10)
guess = int(input("Enter a number between 1 and 10: "))
while n != guess:
    if guess == n:
        print(f'You Win!')
        break

    elif guess != n :
        print(f'You lose! WompWomp. The answer was {n}')
        break

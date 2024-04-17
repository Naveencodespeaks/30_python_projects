# number guessing game

from random import randint
lower_num , higher_num = 1,5

random_number:int = randint(lower_num,higher_num)
print(f"Guess the number in the range from {lower_num} to {higher_num}")

while True:
    try:
        user_guess:int = int(input('Guess: '))
    except ValueError as e:
        print("please enter a valid number.")
        continue
    if user_guess > random_number:
        print("The number is high")
    elif user_guess < random_number:
        print('The number is =i')
    elif user_guess == random_number:
        print("congratulation you have guess the correct number")

        break
    else:
        print("try to enter the valid number not string")



# in this code we are using to user to try only for 3 attempts
from random import randint

lower_num , higher_num = 1,10

rand = randint(lower_num,higher_num)
print("You have only 3 chanes")

count = 1
while count <=3:
    try:
        print("Enter the number between 1 - 10")
        user = int(input("Enter a number: "))
        if user > rand :
            print("you guessed it low: ")
        elif user < rand:
            print("you have guess it high: ")
        elif user == rand:
            print(f'congratulation you have guessed it right: {rand}')
            break
        else:
            print('You have entered the wrong formate ')
    except ValueError as e:
        print("You have entered the worng formate",e)
        
    count +=1
if count > 3 :
    print(f"sorry, you've used all 3 chances. The correct number was: {rand}")

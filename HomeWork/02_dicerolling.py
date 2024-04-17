# roll the dice of diffent numbers

import random

def rolling_dice(num :int = 2)->int:
    if num <=0:
        raise ValueError
    roll = []
    for i in range(num):
        random_roll = random.randint(1,6)
        roll.append(random_roll)
    return roll
def main():
    while True:
        try:
            user_input = input("Enter a dice number you want to role: ")
            if user_input.lower() == "exit": 
                print("Thank you for playing.")
                break
            print(rolling_dice(int(user_input)))
        except ValueError as e:
            print("please enter the valied number: ")

if __name__ == "__main__":
    main()

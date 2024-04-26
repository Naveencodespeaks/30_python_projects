import random 
import sys

class RPS:
    def __init__(self):
        print("welcome to RPS 9000!")
        self.moves:dict ={'rock': '🪨', 'paper' : '📄', 'scissors' : '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())



    def play_game(self):
        user_move:str = input('ROCK, PAPER or SCISSORS ? >>').lower()# Rock -> rock
        if user_move == 'exit':
            print("Thanks for playing")
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()
        
        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move,ai_move)
        self.check_move(user_move,ai_move)



    def display_moves(self,user_move:str, ai_moves: str):
        print('----------------------')
        print(f'you {self.moves[user_move]}')
        print(f'AI {self.moves[ai_moves]}')
        print('--------------')

    def check_move(self,user_move:str, ai_move: str):
        if user_move == ai_move:
            print("its's tie")
        elif user_move == "rock" and ai_move == "scissors":
            print('you win!')
        elif user_move == "scissors" and ai_move == "paper":
            print('you win!')
        elif user_move == "paper" and ai_move == "rock":
            print('you win!')
        else:
            print("AI wins....")


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()



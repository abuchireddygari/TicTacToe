# TicTacToe using AI

import numpy as np
import random
from time import sleep

class TicTacToe:
    board = []
    num_players = 0
    def __init__(self, size:int, num_players:int):
        self.board = [[0 for i in range(size)] for i in range(size)]
        self.num_players = num_players
        print(self.board)
        
    def available_positions(self):
        ap = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                
                if self.board[i][j]==0:
                    ap.append((i,j))
        return ap
    
    def random_position(self, player):
        chosen_position_i, chosen_position_j = random.choice(self.available_positions())
        #print(str(chosen_position_i)+ ' '+str(chosen_position_j))
        self.board[chosen_position_i][chosen_position_j] = player
        return self.board
        
    def row_win(self, player):
        for i in range(len(self.board)):
            win = True
            for j in range(len(self.board)):
                if self.board[i][j] != player:
                    win = False
                    continue
                
            if win == True:
                return win
            
        return win
        
    def col_win(self, player):
        for i in range(len(self.board)):
            win = True
            for j in range(len(self.board)):
                if self.board[j][i] != player:
                    win = False
                    continue
                
            if win == True:
                return win
            
        return win
        
    def diag_win(self, player):
        win = True
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                win = False
                
        return win
    
    def is_board_full(self):
        is_full = True
        for i in range(len(self.board)):
                if  0 in self.board[i]:
                    is_full = False
                    return is_full
                
        return is_full
        
    
    def check_win(self):
        winner  = 0
        for player in range(1,self.num_players+1):
            if self.row_win(player) or self.col_win(player) or self.diag_win(player):
                winner = player
                return winner
            
            if self.is_board_full() and winner == 0:
                winner = -1
                return winner
                
        return winner
            
        
    def play_game(self):
        winner = 0
        num_steps = 0
        
        while not winner:
            for player in range(1,self.num_players+1):
                print(str(player) + ' player turn')
                print(self.random_position(player))
                num_steps+=1
                winner = self.check_win()
                if winner!=0:
                    break
        return winner
    

def main():
    board_size = input('size of the board: ')
    num_players = input('no of players: ')
    play = True
    while(play):
        test = TicTacToe(int(board_size), int(num_players))
        print('winner of the game is '+ str(test.play_game()))
        
        continue_play = input('Continue play y/n?: ')
        if continue_play.lower()=='y':
            play= True
        else:
            play = False
            
        sleep(1)
        
if __name__== "__main__":
    main()
#test = TicTacToe(3)
#print(test.available_positions())
#test.random_position(1)

                 
        
    
    
    

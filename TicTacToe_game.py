import random
import os

def clear_screen():
    
    '''
    Clear output
    '''
    os.system('cls')


def display_board(board):
    '''
    Display the board
    '''
    clear_screen()
    
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])




def toss(P1,P2):
    '''
    Toss and decide which player will go first
    '''
    if random.randint(0,1)==1:
        return P1
    else:
        return P2


def chooseFirst(plyrName):
    '''
    Player1 Choose the mark
    '''
    mark=''
    while mark!='x' and mark!='o':
        mark=input(plyrName+" Please choose your mark 'x' or 'o' : ").lower()
        
    if mark=='x':
        return ('x','o')
    else:
        return ('o','x')
    
    
def enterPosition(board):
    '''
    Ask the position of mark (between 1-9)
    '''

    pos=0
    while (pos not in range (1,10)) or (board[pos]!=' '):
        
        # in case if user put some unexected value
        while True:
            try:
                pos=int(input("Enter number between 1-9 : "))
                break
            except:
                continue
    return pos


def updateBoard(board,coordinate,playerMark):
    '''
    Update the board with mark at given position
    '''
    board[coordinate]=playerMark
    
    
def full_board_check(board):
    '''
    Check if board is full
    '''

    for i in range(1,10):
        if board[i]==' ':
            return False
    return True


def win_check(board,mark):
    '''
    Check if all element of any raw, column or diagonal have given mark
    '''

    if board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:
        return True
    else:
        return False
    
def replay():
    '''
    Ask if player want to rematch
    '''

    return input('If you want to play again press y else press any other key').lower()=='y'
    


def main():
    print("Welcome to Tic Tac Toe Game....!!!!!!!!!!!!!!")

    #Start the game..
    
    while True:
        
        #set the board
        board=[" "]*10
        Player_1=''
        Player_2=''
        
        while len(Player_1)==0:
            Player_1=input('Player 1 please enter your name : ')
        
        while len(Player_2)==0:
            Player_2=input('Player 2 please enter your name : ')
        
        
        # Toss to decide who goes first
        turn=toss(Player_1,Player_2)
        print(turn+" You won the toss, you will start the game !!!")
        
        # Assign marker
        mark1,mark2=chooseFirst(turn)
        
        if turn==Player_1:
            print(Player_1+ " your mark is "+mark1)
            print(Player_2+ " your mark is "+mark2)
        else:
            print(Player_2+ " your mark is "+mark1)
            print(Player_1+ " your mark is "+mark2)
        
      
        
        while True:
            
            if turn==Player_1:
                display_board(board)
                print(Player_1+' its your turn give the location of your '+mark1)
                
                position=enterPosition(board)
                updateBoard(board,position,mark1)
                display_board(board)
                
                if win_check(board,mark1):
                    print(Player_1+" Congratulation you won the game...!!! ")
                    break
                else:
                    if full_board_check(board):
                        print('Game draw....!!')
                        break
                    else:
                        turn=Player_2
                
            else:
                display_board(board)
                print(Player_2+' its your turn give the location of your '+mark2)
                position=enterPosition(board)
                updateBoard(board,position,mark2)
                display_board(board)
                
                if win_check(board,mark2):
                    print(Player_2+" Congratulation you won the game...!!! ")
                    break
                else:
                    if full_board_check(board):
                        print('Game draw....!!')
                        break
                    else:
                        turn=Player_1
                        
        if not replay():
            break
        
        
if __name__=="__main__":
    main()
import random
def print_board(value):
#function to print tic tac toe board
    i=0
    while(i<6):
        if value[i]=='X' or value[i]=='O': 
            if i==2 or i==5:
                print(f"__{value[i]}__")
            else:
                print(f"__{value[i]}__",end='|')
            i+=1
        else:
            if i==2 or i==5:
                print("_____")
            else:
                print("_____",end='|')
            i+=1
    while i<9:
        if value[i]=='X' or value[i]=='O' :
            if i!=8:
                print(f"  {value[i]}  |",end='')
            else:
                print(f"  {value[i]}  ")
        else:
            if i!=8:
                print("     |",end='')
            else:
                print("     ")
        i+=1
def player1_shape():
    choice = 1
    pType=''
    while choice ==1:
        pType = input("Hello player 1. Would you like to be X's or O's? (Enter X or O)\n")
        if pType=='X' or pType == 'O':
            print(f"You have chosen to be {pType}.")
            choice=0  
        else:
            print("That is not a valid choice.")
            print(pType)
    return pType
def player2_shape(p1):
    if p1 == 'X':
        print("Player 2 is O.")
        return 'O'
    else:
        print("Player 2 is X")
        return 'X'
def explain_rules():
    example_values = [1,2,3,4,5,6,7,8,9]
    print("You must get three in a row in any line to win. ")
    print("I will randomly decide which player goes first. ")
    print("First, I will ask for which position you would like to play your shape in.")
    print("The spaces are in the following format:")
    print("__1__|__2__|__3__")
    print("__4__|__5__|__6__")
    print("  7  |  8  |  9  ")
    print("I will then make it the next player's turn and determine a winner if that happens.")
def who_goes_first():
    print("I will now randomly decide which player goes first.")
    prio = random.randint(0,1)
    if(prio==0):
        print("Player 1 will go first.")
        return 0
    else:
        print("Player 2 will go first.")
        return 1
def judge(value):
    if((value[0]==value[1] and value[0]==value[2])and value[0]!=''):
        print("Three in a row at the top.")
        return 1
    elif((value[3] ==value[4] and value[3]==value[5])and value[3]!=''):
        print("Three in a row in the middle")
        return 1
    elif((value[6] ==value[7] and value[6]==value[8])and value[6]!=''):
        print("Three in a row at the bottom")
        return 1
    elif((value[0] ==value[3] and value[0]==value[6])and value[0]!=''):
        return 1
    elif((value[1] ==value[4] and value[1]==value[7])and value[1]!=''):
        return 1
    elif((value[2] ==value[5] and value[2]==value[8])and value[2]!=''):
        return 1
    elif((value[0] ==value[4] and value[0]==value[8])and value[0]!=''):
        return 1
    elif((value[2] ==value[4] and value[2]==value[6])and value[2]!=''):
        return 1
    else:
        return 0





def play_game(p1,p2,prio,value):
    move = 0
    spots = [1,2,3,4,5,6,7,8,9]
    i=0
    valid = 0
    winner =0
    while i<9:
        if(prio==0):
            while valid == 0:
                move = int(input(f"Player 1, which position do you want to put an {p1} at?\n"))
                if move in spots:
                    value[move-1]=p1
                    valid = 1
                    print(f"Player 1 has put an {p1} at spot {move}")
                    spots.remove(move)
                else:
                    print("That spot has already been taken or isn't an option. Try again. ")
            print_board(value)
            winner=judge(value)
            if(winner==1):
                print("Player 1 wins!")
                i=9
            prio=1
            i+=1
            valid = 0
        else:
            while(valid==0):
                move = int(input(f"Player 2, which position do you want to put an {p2} at?\n"))
                if move in spots:
                    value[move-1]=p2
                    valid = 1
                    print(f"Player 2 has put an {p2} at spot {move}")
                    spots.remove(move)
                else:
                    print("That spot has already been taken or isn't an option. Try again. ")
            print_board(value)
            winner=judge(value)
            if(winner==1):
                print("Player 2 wins!")
                i=9
            prio=0
            i+=1
            valid= 0
    print("Game over.")
    if winner==0:
        print("It was a tie.")
    
        

def main():
    p1 = player1_shape()
    p2 = player2_shape(p1)
    explain_rules()
    prio = who_goes_first()
    value=['','','','','','','','','']
    play_game(p1,p2,prio,value)
main()
import random

board={7:" ",8:" ",9:" ",
       4:" ",5:" ",6:" ",
       1:" ",2:" ",3:" "}

def display(board): #Step1
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[1]+"|"+board[2]+"|"+board[3])

def X_O(): #Step2
    cl=["X","O"]
    ci=False
    while   ci==False :
        c=input("Choice X or O:\n")
        c=c.upper()
        if c not in cl:
            print("Sorry that choice is wrong")
        else:
            ci=True
    return(c)

def first(): #Step5
    f=(random.randint(1,2))
    c=""
    if f==1:
        print("X is firts")
        c="X"
    else:
        print("O is firts")
        c="O"
    return (c)

def position():#Step3
    l=range(1,10)
    p="WRONG"
    pi=False
    while p.isdigit()==False or pi==False :

        p=input("Please enter a position (1-9):\n")

        if p.isdigit()==False: 
            print("Sorry that is not a digit")
        
        elif int(p) not in l:
            print("Sorry that position is wrong")
        
        if  (p.isdigit()==True):
            if int(p) in l:
                pi=True
    return (int(p))

def check_position_free(p,board): #Step6
    
    if (board[p]==" "):
            c_p_f=True
    else:
            c_p_f=False
    
    while c_p_f==False:
        
        print("this position is already full")
        p=position()
        c_p_f=check_position_free(p,board)
    
    return(p)
       
def maker(board,c,p): #Step3

    for i in board.keys():
        if i==p:
            board[i]=c
    board=board
    display(board)
    return(board)

def check_win(board): #Step4
    win=""
    if board[7]==board[8]==board[9]!=" ": 
        print("congratulation,")
        win=True

    elif board[4]==board[5]==board[6]!=" ": 
        print("congratulation")
        win=True

    elif board[1]==board[2]==board[3]!=" ": 
        print("congratulation")
        win=True
    
    elif board[1]==board[4]==board[7]!=" ": 
        print("congratulation")
        win=True

    elif board[2]==board[5]==board[8]!=" ": 
        print("congratulation")
        win=True

    elif board[3]==board[6]==board[9]!=" ": 
        print("congratulation")
        win=True

    elif board[1]==board[5]==board[9]!=" ": 
        print("congratulation")
        win=True

    elif board[3]==board[5]==board[7]!=" ": 
        print("congratulation")
        win=True
        
    else:
        win=False

    return (win)

def check_full(board): #Step7
    e=0
    f=0
    for i in board.values():
        if (i==" "):
                e+=1
        else: 
                f+=1
    if e>0:
        full=False

    if f==9:
        print("Draw, board full\nGAME OVER")
        full=True
    
    return(full)

def player(c):

    if c=="O":
        c="x"
    else:
        c="O"
    
    return(c)

def next_move(win,full,board,c):
    for i in range (9):
        print(f"{c.upper()} it's your turn")
        print("What is your next move:")
        p=position()
        check_position_free(p,board)
        board=maker(board,c,p)
        win=check_win(board)
        full=check_full(board)
        c=player(c)
        if win==True or full==True:
            break
        else:
            i+=1

def replay():
    cl=["Y","N"]
    ci=False
    while   ci==False :
        print('Do you want to play again?')
        c=input("Choice Y or N:\n")
        c=c.upper()
        if c not in cl:
            print("Sorry that choice is wrong")
        else:
            ci=True
    return(c.startswith("Y"))

while True:
    board={7:" ",8:" ",9:" ",
           4:" ",5:" ",6:" ",
           1:" ",2:" ",3:" "}
    display(board)
    c=first()
    p=position()
    check_position_free(p,board)
    board=maker(board,c,p)
    win=check_win(board)
    full=check_full(board)
    c=player(c)
    next_move(win,full,board,c)

    if not replay():
        break
import random
randNo = random.randint(1,3)

def gameWin(Comp,Player):
    if Comp == Player:
        return None
    elif Comp == 'R':
        if Player=='P':
            return True
        elif Player=='S':
            return False
    elif Comp == 'P':
        if Player=='S':
            return True
        elif Player=='R':
            return False
    elif Comp == 'S':
        if Player=='R':
            return True
        elif Player=='P':
            return False
    
    

Comp = print("Computer's turn: Rock(R) Paper(P) or Sissors(S)")
if randNo == 1:
    Comp = 'R'
elif randNo == 2:
    Comp = 'P'
elif randNo ==3:
    Comp = 'S'
    
Player = input("Choose Rock(R) Paper(P) or Sissors(S): ")
print ("Computer Chose "+str(Comp))

gameResult =gameWin(Comp,Player)
if gameResult == True:
    print("You win") 
elif gameResult == False:
    print("You Loose")
elif gameResult == None:
    print("It's a tie")          

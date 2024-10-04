import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
1.yes
2.NO|Exits                 '''))
    if uc==1:
        for a in range(1,6):

            user_input=int(input('''
1.rock
2.paper
3.scissor                                                          '''))
            if user_input==1:
                uchoice="rock"
            elif user_input==2:
                 uchoice="paper"
            elif user_input==3:
                 uchoice="scissor"
            cchoice=random.choice(l)    
            if uchoice==cchoice:
               print("GAME-DRAW")
               print("user value",uchoice)
               print("computer value",cchoice)
               ucount=ucount+1
               ccount=ccount+1
            if (uchoice=="rock"and cchoice=="scissor")or(uchoice
                                                     =="paper"and cchoice=="rock")or(uchoice=="scissor"and cchoice=="paper"):
               print("YOU WIN THE GAME")
               print("user value",uchoice)
               print("computer value",cchoice)
               ucount=ucount+1
            else:
                print("COMPUTER WIN THE GAME")
                print("user value",uchoice)
                print("computer value",cchoice)
                ccount=ccount+1
        if ccount==ucount:
            print("final game =DRAW") 
            print("user value",ucount)
            print("computer value",ccount)   
        elif ccount>ucount:
            print("final game= COMPUTER WIN")
            print("user value",ucount)
            print("computer value",ccount)
        else:
            print("final game= YOU WIN")
            print("user value",ucount)
            print("computer value",ccount)

    else:
        break
                        
            
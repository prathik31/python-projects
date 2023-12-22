import random

print("lets play rock ,paper and sissors in python!!!!")

def start():
    print("choice 1: ROCK")
    print("choice 2: PAPER")
    print("choice 3: SISSORS")

    choice=int(input("enter your choice(1-3):"))
  
    if choice==1:
        print('YOU HAVE CHOSEN:     ROCK')
    elif choice==2:
        print("YOU HAVE CHOSEN:     PAPER")
    elif choice==3:
        print("YOU HAVE CHOSEN:     SISSORS")
    else:
        print("enter the choice between 1-3")
       
    com_choi=random.randint(1,3)

    if com_choi==1:
        print('COMPUTER HAS CHOSEN:     ROCK')
    elif com_choi==2:
        print("COMPUTER HAS CHOSEN:     PAPER")
    elif com_choi==3:
        print("COMPUTER HAS CHOSEN:     SISSORS")

    if choice==com_choi:
        print("its a tie")
    if (choice==1) and (com_choi==2):
        print("you lost")
    if (choice==1) and (com_choi==3):
        print("you won")
    if (choice==2) and (com_choi==1):
        print("you won")
    if (choice==2) and (com_choi==3):
        print("you lost")
    if (choice==3) and (com_choi==1):
        print("you lost")
    if (choice==3) and (com_choi==2):
        print("you won")

play=True

while play:
    start()
    c=input("do you want to continue(y/n):")
    if c=='y':
        play=True
    else:
        play=False
        print("THANK YOU!!")


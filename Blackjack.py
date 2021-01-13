from random import sample
import random
print(" Welcome to the game of Blackjack, you will start with 1000 dollars, good luck.")
AceOfHearts = 10
AceOfSpades = 10
AceOfDiamonds = 10
AceOfClubs = 10
AIAceOfHearts = 10
AIAceOfSpades = 10
AIAceOfDiamonds = 10
AIAceOfClubs = 10
deck = ["Ace Of Hearts", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Clubs"
    , "Two Of Hearts", "Two Of Spades", "Two Of Diamonds", "Two Of Clubs"
    , "Three Of Hearts", "Three Of Spades", "Three Of Diamonds", "Three Of Clubs"
    , "Four Of Hearts", "Four Of Spades", "Four Of Diamonds", "Four Of Clubs"
    , "Five Of Hearts", "Five Of Spades", "Five Of Diamonds", "Five Of Clubs"
    , "Six Of Hearts", "Six Of Spades", "Six Of Diamonds", "Six Of Clubs"
    , "Seven Of Hearts", "Seven Of Spades", "Seven Of Diamonds", "Seven Of Clubs"
    , "Eight Of Hearts", "Eight Of Spades", "Eight Of Diamonds", "Eight Of Clubs"
    , "Nine Of Hearts", "Nine Of Spades", "Nine Of Diamonds", "Nine Of Clubs"
    , "Ten Of Hearts", "Ten Of Spades", "Ten Of Diamonds", "Ten Of Clubs"
    , "Jack Of Hearts", "Jack Of Spades", "Jack Of Diamonds", "Jack Of Clubs"
    , "Queen Of Hearts", "Queen Of Spades", "Queen Of Diamonds", "Queen Of Clubs"
    , "King Of Hearts", "King Of Spades", "King Of Diamonds", "King Of Clubs"]
random.shuffle(deck)
playercurrenthand=[]
AIcurrenthand=[]
playercount=0
Aicount=0
def f3():
    global deck
    global playercount
    playercount=0
    if playercurrenthand[0][0:3] == "Ace":
        playercount+= 11
    if playercurrenthand[0][0:3] == "Two":
        playercount+=2
    if playercurrenthand[0][0:5] == "Three":
        playercount+=3
    if playercurrenthand[0][0:4] == "Four":
        playercount+=4
    if playercurrenthand[0][0:4] == "Five":
        playercount+=5
    if playercurrenthand[0][0:3] == "Six":
        playercount+=6
    if playercurrenthand[0][0:5] == "Seven":
        playercount+=7
    if playercurrenthand[0][0:5] == "Eight":
        playercount += 8
    if playercurrenthand[0][0:4] == "Nine":
        playercount += 9
    if playercurrenthand[0][0:3] == "Ten":
        playercount += 10
    if playercurrenthand[0][0:4] == "Jack":
        playercount += 10
    if playercurrenthand[0][0:5] == "Queen":
        playercount += 10
    if playercurrenthand[0][0:4] == "King":
        playercount += 10
    if playercurrenthand[1][0:3] == "Ace":
        playercount+= 11
    if playercurrenthand[1][0:3] == "Two":
        playercount+=2
    if playercurrenthand[1][0:5] == "Three":
        playercount+=3
    if playercurrenthand[1][0:4] == "Four":
        playercount+=4
    if playercurrenthand[1][0:4] == "Five":
        playercount+=5
    if playercurrenthand[1][0:3] == "Six":
        playercount+=6
    if playercurrenthand[1][0:5] == "Seven":
        playercount+=7
    if playercurrenthand[1][0:5] == "Eight":
        playercount += 8
    if playercurrenthand[1][0:4] == "Nine":
        playercount += 9
    if playercurrenthand[1][0:3] == "Ten":
        playercount += 10
    if playercurrenthand[1][0:4] == "Jack":
        playercount += 10
    if playercurrenthand[1][0:5] == "Queen":
        playercount += 10
    if playercurrenthand[1][0:4] == "King":
        playercount += 10
    if playercurrenthand[0][0:3] == "Ace" and playercurrenthand[1][0:3] == "Ace":
        playercount=12
        if playercurrenthand[0] == "Ace Of Hearts":
            global AceOfHearts
            AceOfHearts = 0
        if playercurrenthand[0] == "Ace Of Spades":
            global AceOfSpades
            AceOfSpades = 0
        if playercurrenthand[0] == "Ace Of Diamonds":
            global AceOfDiamonds
            AceOfDiamonds = 0
        if playercurrenthand[0] == "Ace Of Clubs":
            global AceOfClubs
            AceOfClubs = 0
    if playercount==21:
        print(("You got 21, wait to see will AI match"))
    else:
        print("Your current count is", playercount)
        print("Do you wish to draw another card? Please answer with Yes or No.")
        YesOrNo=input()
        while YesOrNo!="No":
            playercurrenthand.append(deck.pop())
            if playercurrenthand[-1][0:3] == "Ace":
                print("You draw", playercurrenthand[-1])
                playercount += 11
            if playercurrenthand[-1][0:3] == "Two":
                print ("You draw ",playercurrenthand[-1])
                playercount += 2
            if playercurrenthand[-1][0:5] == "Three":
                print("You draw ", playercurrenthand[-1])
                playercount += 3
            if playercurrenthand[-1][0:4] == "Four":
                print("You draw ", playercurrenthand[-1])
                playercount += 4
            if playercurrenthand[-1][0:4] == "Five":
                print("You draw ", playercurrenthand[-1])
                playercount += 5
            if playercurrenthand[-1][0:3] == "Six":
                print("You draw ", playercurrenthand[-1])
                playercount += 6
            if playercurrenthand[-1][0:5] == "Seven":
                print("You draw ", playercurrenthand[-1])
                playercount += 7
            if playercurrenthand[-1][0:5] == "Eight":
                print("You draw ", playercurrenthand[-1])
                playercount += 8
            if playercurrenthand[-1][0:4] == "Nine":
                print("You draw ", playercurrenthand[-1])
                playercount += 9
            if playercurrenthand[-1][0:3] == "Ten":
                print("You draw ", playercurrenthand[-1])
                playercount += 10
            if playercurrenthand[-1][0:4] == "Jack":
                print("You draw ", playercurrenthand[-1])
                playercount += 10
            if playercurrenthand[-1][0:5] == "Queen":
                print("You draw ", playercurrenthand[-1])
                playercount += 10
            if playercurrenthand[-1][0:4] == "King":
                print("You draw ", playercurrenthand[-1])
                playercount += 10
            if playercount > 21 and "Ace Of Hearts" in playercurrenthand:
                playercount-=AceOfHearts
                AceOfHearts=0
            if playercount > 21 and "Ace Of Spades" in playercurrenthand:
                playercount-=AceOfSpades
                AceOfSpades=0
            if playercount > 21 and "Ace Of Diamonds" in playercurrenthand:
                playercount -= AceOfDiamonds
                AceOfDiamonds=0
            if playercount > 21 and "Ace Of Clubs" in playercurrenthand:
                playercount -= AceOfClubs
                AceOfClubs=0
            if playercount == 21:
                print(("You got 21, wait to see will AI match"))
                break
            if playercount > 21:
                print("You went over 21, you lost.")
                Player1.loss()
                break
            print("Your current count is", playercount)
            print("Do you wish to draw another card? Please answer with Yes or No.")
            YesOrNo = input()
def f4():
    global Aicount
    Aicount=0
    global deck
    if AIcurrenthand[0][0:3] == "Ace":
        Aicount+= 11
    if AIcurrenthand[0][0:3] == "Two":
        Aicount+=2
    if AIcurrenthand[0][0:5] == "Three":
        Aicount+=3
    if AIcurrenthand[0][0:4] == "Four":
        Aicount+=4
    if AIcurrenthand[0][0:4] == "Five":
        Aicount+=5
    if AIcurrenthand[0][0:3] == "Six":
        Aicount+=6
    if AIcurrenthand[0][0:5] == "Seven":
        Aicount+=7
    if AIcurrenthand[0][0:5] == "Eight":
        Aicount += 8
    if AIcurrenthand[0][0:4] == "Nine":
        Aicount += 9
    if AIcurrenthand[0][0:3] == "Ten":
        Aicount += 10
    if AIcurrenthand[0][0:4] == "Jack":
        Aicount += 10
    if AIcurrenthand[0][0:5] == "Queen":
        Aicount += 10
    if AIcurrenthand[0][0:4] == "King":
        Aicount += 10
    if AIcurrenthand[1][0:3] == "Ace":
        Aicount+= 11
    if AIcurrenthand[1][0:3] == "Two":
        Aicount+=2
    if AIcurrenthand[1][0:5] == "Three":
        Aicount+=3
    if AIcurrenthand[1][0:4] == "Four":
        Aicount+=4
    if AIcurrenthand[1][0:4] == "Five":
        Aicount+=5
    if AIcurrenthand[1][0:3] == "Six":
        Aicount+=6
    if AIcurrenthand[1][0:5] == "Seven":
        Aicount+=7
    if AIcurrenthand[1][0:5] == "Eight":
        Aicount += 8
    if AIcurrenthand[1][0:4] == "Nine":
        Aicount += 9
    if AIcurrenthand[1][0:3] == "Ten":
        Aicount += 10
    if AIcurrenthand[1][0:4] == "Jack":
        Aicount += 10
    if AIcurrenthand[1][0:5] == "Queen":
        Aicount += 10
    if AIcurrenthand[1][0:4] == "King":
        Aicount += 10
    if AIcurrenthand[0][0:3] == "Ace" and AIcurrenthand[1][0:3] == "Ace":
        Aicount=12
        if AIcurrenthand[0] == "Ace Of Hearts":
            global AIAceOfHearts
            AIAceOfHearts = 0
        if AIcurrenthand[0] == "Ace Of Spades":
            global AIAceOfSpades
            AIAceOfSpades = 0
        if AIcurrenthand[0] == "Ace Of Diamonds":
            global AIAceOfDiamonds
            AIAceOfDiamonds = 0
        if AIcurrenthand[0] == "Ace Of Clubs":
            global AIAceOfClubs
            AIAceOfClubs = 0
    print("AI draws " ,AIcurrenthand[0], "and", AIcurrenthand[1])
    print("AI count is currently ",Aicount)
    if Aicount > playercount:
        Player1.loss()
        print("You lost")
    if Aicount == playercount:
        print("It's a draw")
    if Aicount==21:
        if playercount == 21:
            print("It's a draw")
    if Aicount<21:
            while Aicount < playercount:
                AIcurrenthand.append(deck.pop())
                if AIcurrenthand[-1][0:3] == "Ace":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 11
                if AIcurrenthand[-1][0:3] == "Two":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 2
                if AIcurrenthand[-1][0:5] == "Three":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 3
                if AIcurrenthand[-1][0:4] == "Four":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 4
                if AIcurrenthand[-1][0:4] == "Five":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 5
                if AIcurrenthand[-1][0:3] == "Six":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 6
                if AIcurrenthand[-1][0:5] == "Seven":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 7
                if AIcurrenthand[-1][0:5] == "Eight":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 8
                if AIcurrenthand[-1][0:4] == "Nine":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 9
                if AIcurrenthand[-1][0:3] == "Ten":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 10
                if AIcurrenthand[-1][0:4] == "Jack":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 10
                if AIcurrenthand[-1][0:5] == "Queen":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 10
                if AIcurrenthand[-1][0:4] == "King":
                    print("AI draws", AIcurrenthand[-1])
                    Aicount += 10
                if Aicount > 21 and "Ace Of Hearts" in AIcurrenthand:
                    Aicount-=AIAceOfHearts
                    AIAceOfHearts=0
                if Aicount > 21 and "Ace Of Spades" in AIcurrenthand:
                    Aicount-=AIAceOfSpades
                    AIAceOfSpades=0
                if Aicount > 21 and "Ace Of Diamonds" in AIcurrenthand:
                    Aicount -= AIAceOfDiamonds
                    AIAceOfDiamonds=0
                if Aicount > 21 and "Ace Of Clubs" in AIcurrenthand:
                    Aicount -= AIAceOfClubs
                    AIAceOfClubs=0
                print("AI count is currently", Aicount)
                if Aicount == 21 and playercount < 21:
                    print(("AI won"))
                    Player1.loss()
                    break
                if Aicount > 21:
                    print("AI went over 21, you won.")
                    Player1.won()
                    break
                if Aicount > playercount:
                    print("You lost")
                    Player1.loss()
                if Aicount == playercount:
                    print("It's a draw")
class Player:
    global money
    global deck
    def __init__(self,money):
        self.money = money
    def loss(self):
        self.money -= bet
    def won(self):
        self.money += bet
    def balance(self):
        print("You currently have available ", self.money, "dollars" )
    def player_draw(self):
        playercurrenthand.append(deck.pop(0))
        playercurrenthand.append(deck.pop(0))
        print("You draw", playercurrenthand[0], "and", playercurrenthand[1])
    def AI_draw(self):
        AIcurrenthand.append(deck.pop(0))
        AIcurrenthand.append(deck.pop(0))
        print("AI draws",AIcurrenthand[0], "and a hidden card ")
    def playagain(self):
        global deck
        print("Do you want to play again, please answer with Yes or No")
        DoYouWantToPlayAgain = input()
        while DoYouWantToPlayAgain != "No":
            global playercurrenthand
            playercurrenthand = []
            global AIcurrenthand
            AIcurrenthand = []
            print("Please enter your bet")
            global bet
            bet = int(input())
            Dealer.AI_draw()
            Player1.player_draw()
            f3()
            if playercount < 21:
                print("You decided to check, your current count is ", playercount, ", wait to see count of AI")
            if playercount < 21 or playercount == 21:
                f4()
            Player1.balance()
            print("Do you want to play again? Please answer with Yes or No")
            DoYouWantToPlayAgain = input()
            if len(deck)<20:
                deck = ["Ace Of Hearts", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Clubs"
                    , "Two Of Hearts", "Two Of Spades", "Two Of Diamonds", "Two Of Clubs"
                    , "Three Of Hearts", "Three Of Spades", "Three Of Diamonds", "Three Of Clubs"
                    , "Four Of Hearts", "Four Of Spades", "Four Of Diamonds", "Four Of Clubs"
                    , "Five Of Hearts", "Five Of Spades", "Five Of Diamonds", "Five Of Clubs"
                    , "Six Of Hearts", "Six Of Spades", "Six Of Diamonds", "Six Of Clubs"
                    , "Seven Of Hearts", "Seven Of Spades", "Seven Of Diamonds", "Seven Of Clubs"
                    , "Eight Of Hearts", "Eight Of Spades", "Eight Of Diamonds", "Eight Of Clubs"
                    , "Nine Of Hearts", "Nine Of Spades", "Nine Of Diamonds", "Nine Of Clubs"
                    , "Ten Of Hearts", "Ten Of Spades", "Ten Of Diamonds", "Ten Of Clubs"
                    , "Jack Of Hearts", "Jack Of Spades", "Jack Of Diamonds", "Jack Of Clubs"
                    , "Queen Of Hearts", "Queen Of Spades", "Queen Of Diamonds", "Queen Of Clubs"
                    , "King Of Hearts", "King Of Spades", "King Of Diamonds", "King Of Clubs"]
                random.shuffle(deck)
                print("The deck has reseted")


Player1=Player(1000)
Dealer=Player(1000000)
print("Please enter your bet")
bet=int(input())
Dealer.AI_draw()
Player1.player_draw()
f3()
if playercount < 21:
    print("You decided to check, your current count is ",playercount, ", wait to see count of AI")
if playercount <21:
    f4()
if playercount == 21:
    f4()
Player1.balance()
Player1.playagain()

print("Thank you for playing")



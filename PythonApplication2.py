playGame='Y'
class Player(object):
    def __init__(self, bal_amt=1000):
        self.bal_amt=bal_amt
        self.count=0
        self.action='H'

    def betAmt(self,bet_amt):
        self.bet_amt=int(bet_amt)

    def balAmt(self,bet_amt,win_lose):
        if(win_lose==True):
            self.bal_amt += 2*bet_amt
        elif(win_lose==False):
            self.bal_amt-=bet_amt
    
    def display(self):
         print('Player Count is %d' %(self.count))


from random import choice

class Deck(object):
    deck=[2,3,4,5,6,7,8,9,10,'K','J','Q','A']

    def __init__(self):
        self.dict = {}
        for i in Deck.deck:
            self.dict[i]=4
    
    def selectCard(self):
        var = choice(Deck.deck)
        self.dict[var]-=1
        if self.dict[var] == 0 :
            selectCard(self)

        if var in ('K','J','Q'):
            return 10
        elif var == 'A':
            return 11
        else: return var

class Dealer(object):
    def __init__(self, bal_amt=1000):
        self.bal_amt=bal_amt
        self.count=0
        self.action='H'

    def betAmt(self,bet_amt):
        self.bet_amt = int(bet_amt)

    def balAmt(self,bet_amt,win_lose):
        if(win_lose==True):
            self.bal_amt+=2*bet_amt
        elif(win_lose==False):
            self.bal_amt-=bet_amt

    def display(self):
         print('Dealer Count is %d' %(self.count))

def printBal(player, dealer):
    print('Player Balance %d' %(player.bal_amt))
    print('Dealer Balance %d' %(dealer.bal_amt))

player=Player()
dealer=Dealer()
while(playGame=='Y'):
    player.count
    player.action='H'
    dealer.action='H'
    x=Deck()
    print('Start Blackjack')
    printBal(player, dealer)
    player.betAmt(int(input('Enter bet amount')))
    player.balAmt(player.bet_amt,False)
    dealer.balAmt(player.bet_amt,False)
    printBal(player, dealer)
    for i in range(0,2):
        player.count=x.selectCard()
        dealer.count=x.selectCard()
    player.display()
    dealer.display()
    while((player.count<22 and dealer.count<22) or (player.action=='H' and dealer.action=='H')):
        if(player.action!='S'):
            player.action=input('Player : Select you want to hit or stand? H/S')
            if(player.action=='H'):        
                player_card=x.selectCard()
                if(player_card==11):
                    if(player.count + player_card <22):
                        player.count += player_card
                    else:
                        player.count += 1
            
                else: player.count += player_card
        
            player.display()
        
            if(player.count>21):
                print('Player 1 bust')
                dealer.balAmt(player.bet_amt,True)
                playGame='N'
                playGame=input('Do you want to play a new game?Y/N')
                break

        
        if(dealer.action!='S'):
            if (dealer.count in range(17,22)):
                dealer.action=input('Dealer : Select you want to hit or stand? H/S')
                if(dealer.action=='H'):        
                    dealer_card=x.selectCard()
                    if(dealer_card==11):
                        if(dealer.count + dealer_card <22):
                            dealer.count += dealer_card
                        else:
                            dealer.count += 1
         
                    else: dealer.count += dealer_card

            else:
                dealer_card=x.selectCard()
                if(dealer_card==11):
                    if(dealer.count + dealer_card <22):
                        dealer.count += dealer_card
                    else:
                        dealer.count += 1
         
                else: dealer.count += dealer_card

            dealer.display()

            if(dealer.count>21):
                print('Dealer bust')
                player.balAmt(player.bet_amt,True)
                playGame='N'
                playGame=input('Do you want to play a new game?Y/N')
                break

        if(dealer.action=='S' and player.action=='S'):
            if(dealer.count > player.count):
                print('Dealer wins')
            else: print('Player wins')

            playGame='N'
            playGame=input('Do you want to play a new game?Y/N')
            break

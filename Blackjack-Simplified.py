import random


#Declaring global variables:

Suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

Ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
        'Jack', 'Queen', 'King', 'Ace']

Values = {'Two': 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7,
        'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen': 10, 'King': 10, 'Ace': 11}



# Classes definition


class Card:
    
    '''
    CLass of Cards that contain all the attributes of each card
    and the method to print out the name of the card.

    '''
    def __init__(self, Suit, Rank):
        
        self.suit = Suit
        self.rank = Rank
        self.value = Values[Rank]
        
    def __str__(self):
        
        return f"{self.rank} of {self.suit}"







class Deck:

    '''
    When the object deck gets created the objects cards get instantiated too
    by combining the elements of Suits and Ranks lists.
    '''
    
    def __init__(self):
        
        self.cards_created = []
        
        for suit in Suits:
            for rank in Ranks:
                card_created = Card(suit, rank)
                self.cards_created.append(card_created)
    
    def shuffle(self):

        '''
        Shuffle function imported from random library.
        '''

        random.shuffle(self.cards_created)
    
    def deal_one(self):

        '''
        Pop method on cards_created attribute of the deck object.
        '''
        
        return self.cards_created.pop()
                
    def re_deck(self):

        '''
        Extend method to refill the deck at the end of the hand.

        '''
        self.cards_created.extend(player.cards)
        self.cards_created.extend(dealer.cards)
        player.cards = []
        dealer.cards = []
        random.shuffle(self.cards_created)





class Players:

    '''
    Parent class of Chips. Its attributes and methods are created when 
    an object from Chip class gets instantiated.
    '''
    
    def __init__(self, name):
        
        self.name = name
        
        self.cards = []



    def add_cards(self):


        '''
        Add to cards attribute the first object card from the deck object list.
        '''

        self.cards.append(deck.deal_one())
            
            
        
    
    def sum_value(self):

        '''
        Method that returns the numerical value of a player's hand.
        '''

        value = 0
        for card in self.cards:
            value = value + card.value
        
        return value
    





class Chips(Players):

    '''
    This class contains the method to balance the account of the player
    and dealer. When an object is instantiated, it hereditiates attribute name
    and method from Players parent class.
    '''
    bet = 0

    def __init__(self, initial_amount, name):
        Players.__init__(self,name)
        
        self.balance = initial_amount
        
      
    def make_balance(self):
        '''
        Balance calculation
        '''
        
        self.balance = self.balance - self.bet
        
    def __str__(self):

        '''
        Display amount with print() function call
        '''
        
        return f"{self.name} has a total amount of £{self.balance} \n"

        


'''
Start
'''
  

# Enstablishing name and initial stack. Objects instantiation.
deck = Deck()



player_name = input("What's your name?    ")
initial_amount = int(input('How many ££ would you like to play with?   \n'))
player = Chips(initial_amount, player_name)
dealer = Chips(initial_amount, 'Dealer')

print(player)
print(dealer)

# Starting the match
deck.shuffle()
game_on = True
while game_on:
    
    deck.shuffle()
    if player.balance == 0:
        print(f'{player.name} lost all the money. {player.name} is homeless')
        break
    elif dealer.balance == 0:
        print(f'{dealer.name} lost all the money. {dealer.name} is homeless')
        break
    else:
        pass
    player.bet = int(input("How much do you want to bet in £?  \n"))
    if player.bet > player.balance:
        player.bet = player.balance
    elif player.bet > dealer.balance:
        player.bet = dealer.balance
        print('ALL IN!!!\n')
    else:
        pass
    player.make_balance()
    print(player)
    print(dealer)
    for dealing in range(2):
        player.add_cards()
        dealer.add_cards()
    print(f'{player.name} has {player.cards[0]} and {player.cards[1]} \n')
    print(f'Dealer has {dealer.cards[0]} and covered card \n')
    hit = True
    while hit:
        choice = input("What do you want to do, stay or hit?  Choose 'stay' or 'hit'  ")
        if choice == 'stay':
            hit = False
            break
        else:
            player.add_cards()
            print(f'Your new card is {player.cards[-1]}')
    
    #Checking for ace(s)
    
    for card in player.cards:
        if card.rank == 'Ace':
            card.value = int(input("How much you want your Ace to be valued, 1 or 11?  "))
        else:
            pass
    #Checking player's value
    p_value = player.sum_value()
    if p_value > 21:
        print('BUST! \n')
        print('You lost this hand...')
        deck.re_deck()
    else:
        # Dealer hits
        d_hits_on = True
        while d_hits_on:
            d_value = dealer.sum_value()
            
            if d_value > p_value:
                d_hits_on = False
                if d_value > 21:
                    print(f'Dealer BUSTS, {player.name} won the hand and the bet!')
                    dealer.balance = dealer.balance - player.bet
                    player.balance = player.balance + 2 * player.bet
                    deck.re_deck()
                else:
                    print(f"Dealer won the hand and {player.name}'s money")
                    dealer.balance = dealer.balance + player.bet
                    deck.re_deck()
                    break
                
                
            # Cheching for dealer and player matched value scenario

            elif d_value == 21 and p_value == 21:
                p_blackjack = False
                d_blackjack = False
                for card in player.cards:
                    if card.rank == 'Ace':
                        p_blackjack = True
                    else:
                        pass
                for card in dealer.cards:
                    if card.rank == 'Ace':
                        d_blacjack = True
                if d_blackjack and p_blackjack:
                    player.balance = player.balance + player.bet
                    print(f'Both {player.name} and dealer have Blackjack. How unfortunate!')
                    deck.re_deck()
                elif d_blackjack:
                    dealer.balance = dealer.balance + player.bet
                    print(f'Dealer has Blackjack. You lost your hand...')
                    deck.re_deck()
                elif p_blackjack:
                    dealer.balance = dealer.balance - player.bet
                    player.balance = player.balance + 2*player.bet
                    print(f'WOW! {player.name} has Blackjack. You won this hand!')
                    deck.re_deck()
                else:
                    player.balance = player.balance + player.bet
                    print('It seems that this hand was a tie!')
                    deck.re_deck()
                    break
            else:
                dealer.add_cards()
                    
   

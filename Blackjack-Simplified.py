'''
Module containing classes for the construction of Blackjack game objects, with their fields/attribute and methods.
Import this module and play Blackjack!

'''

import random




# Declaring global variables:

Suits = ['Hearts','Diamonds','Spades','Clubs']

Ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']

Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack' :10, 'Queen': 10, 'King': 10, 'Ace': 11}



# Classes definition #



class Card:
    
    '''
    CLass of Cards that contain all the attributes of each card
    and the method to print out the name of the card.
    '''

    def __init__(self, Suit, Rank):
        
        self.suit= Suit
        self.rank=Rank
        self.value= Values[Rank]
        
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
                card_created = Card(suit,rank)
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
                
    def re_deck(self,player,dealer):

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
        
        self.name=name
        
        self.cards= []



    def add_cards(self,deck):

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

    bet=0

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

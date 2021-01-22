import random

import Blackjack_classes as classes



'''
Start
'''
  

# Enstablishing name and initial stack. Objects instantiation.
deck = classes.Deck()



player_name = input("What's your name?    ")
initial_amount = int(input('How many ££ would you like to play with?   \n'))
player = classes.Chips(initial_amount, player_name)
dealer = classes.Chips(initial_amount, 'Dealer')

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
        player.add_cards(deck)
        dealer.add_cards(deck)
    print(f'{player.name} has {player.cards[0]} and {player.cards[1]} \n')
    print(f'Dealer has {dealer.cards[0]} and covered card \n')
    hit = True
    while hit:
        choice = input("What do you want to do, stay or hit?  Choose 'stay' or 'hit'  ")
        if choice == 'stay':
            hit = False
            break
        else:
            player.add_cards(deck)
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
        deck.re_deck(player, dealer)
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
                    deck.re_deck(player, dealer)
                else:
                    print(f"Dealer won the hand and {player.name}'s money")
                    dealer.balance = dealer.balance + player.bet
                    deck.re_deck(player, dealer)
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
                    deck.re_deck(player, dealer)
                elif d_blackjack:
                    dealer.balance = dealer.balance + player.bet
                    print(f'Dealer has Blackjack. You lost your hand...')
                    deck.re_deck(player, dealer)
                elif p_blackjack:
                    dealer.balance = dealer.balance - player.bet
                    player.balance = player.balance + 2*player.bet
                    print(f'WOW! {player.name} has Blackjack. You won this hand!')
                    deck.re_deck(player, dealer)
                else:
                    player.balance = player.balance + player.bet
                    print('It seems that this hand was a tie!')
                    deck.re_deck(player, dealer)
                    break
            else:
                dealer.add_cards(deck)
                    
   
    

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:54:48 2020

@author: Bill Woloschuk

"""
import os
import random

numlist = list(range(2,11))
strlist = [str(i) for i in numlist]
lowcards = strlist+['J','Q','K']
suits = ['♠','♣','♥','♦']
deck = [x + y for x in lowcards for y in suits]

value = {'2♠': 2, '2♣': 2, '2♥': 2, '2♦': 2,
         '3♠': 3, '3♣': 3, '3♥': 3, '3♦': 3,
         '4♠': 4, '4♣': 4, '4♥': 4, '4♦': 4,
         '5♠': 5, '5♣': 5, '5♥': 5, '5♦': 5,
         '6♠': 6, '6♣': 6, '6♥': 6, '6♦': 6,
         '7♠': 7, '7♣': 7, '7♥': 7, '7♦': 7,
         '8♠': 8, '8♣': 8, '8♥': 8, '8♦': 8,
         '9♠': 9, '9♣': 9, '9♥': 9, '9♦': 9,
         '10♠': 10, '10♣': 10, '10♥': 10, '10♦': 10,
         'J♠': 10, 'J♣': 10, 'J♥': 10, 'J♦': 10,
         'Q♠': 10, 'Q♣': 10, 'Q♥': 10, 'Q♦': 10,
         'K♠': 10, 'K♣': 10, 'K♥': 10, 'K♦': 10}

def deal(deck):
    hand = []
    random.shuffle(deck)
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_cards = []
        player_cards = []
        numlist = list(range(2,11))
        strlist = [str(i) for i in numlist]
        lowcards = strlist+['J','Q','K']
        suits = ['♠','♣','♥','♦']
        deck = [x + y for x in lowcards for y in suits]
        random.shuffle(deck)
        game()
    else:
	    print("Bye!")
	    exit()

#Dealer Cards
dealer_cards = [deck.pop() for i in range(2)]

#Player Cards
player_cards = [deck.pop() for i in range(2)]


def hit(hand):
	card = deck.pop()
	hand.append(card)
	return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
       os.system('clear')

def print_results(dealer_cards, player_cards):
	clear()
	print ("The dealer has ", dealer_cards, " for a total of ", sum(map(value.get,dealer_cards)))
	print ("You have ", player_cards, " for a total of ", sum(map(value.get,player_cards)))

def blackjack(dealer_cards, player_cards):
	if sum(map(value.get,player_cards)) == 21:
		print_results(dealer_cards, player_cards)
		print ("Congratulations! You got Blackjack!\n")
		play_again()
	elif sum(map(value.get,dealer_cards)) == 21:
		print_results(dealer_cards, player_cards)
		print ("Sorry, you lose. The dealer got a blackjack.\n")
		play_again()

def score(dealer_cards, player_cards):
    if sum(map(value.get,player_cards)) == 21:
	    print_results(dealer_cards, player_cards)
	    print ("Congratulations! You got Blackjack!\n")
    elif sum(map(value.get,dealer_cards)) == 21:
	    print_results(dealer_cards, player_cards)
	    print ("Sorry, you lose. The dealer got blackjack.\n")
    elif sum(map(value.get,player_cards)) > 21:
	    print_results(dealer_cards, player_cards)
	    print ("Sorry. You busted. You lose.\n")
    elif sum(map(value.get,dealer_cards)) > 21:
	    print_results(dealer_cards, player_cards)
	    print ("Dealer busts. You win!\n")
    elif sum(map(value.get,player_cards)) <= sum(map(value.get,dealer_cards)):
        print_results(dealer_cards, player_cards)
        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif sum(map(value.get,player_cards)) > sum(map(value.get,dealer_cards)):
	    print_results(dealer_cards, player_cards)
	    print ("Congratulations. Your score is higher than the dealer. You win!\n")

def game():
    choice = 0
    clear()
    print("\n    WELCOME TO BLACKJACK!\n")
    print("\n   This Version has NO ACEs  \n ")	
    dealer_cards = deal(deck)
    player_cards = deal(deck)
    print ("The dealer has one hidden card and is showing", dealer_cards[1])
    print ("You show ", player_cards, " for a total of ", sum(map(value.get,player_cards)))
    blackjack(dealer_cards, player_cards)
    quit=False
    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':
            hit(player_cards)
            print(player_cards, "for a total of", sum(map(value.get,player_cards)))
            if sum(map(value.get,player_cards)) > 21:
                print('You busted')
                play_again()
        elif choice=='s':
            while sum(map(value.get,dealer_cards)) < 17:
                hit(dealer_cards)
                print(dealer_cards)
                if sum(map(value.get,dealer_cards)) > 21:
                    print('Dealer busts, you win!')
                    play_again()
            score(dealer_cards,player_cards)
            play_again()
        elif choice == "q":
            print("Bye!")
            quit=True
            exit()

if __name__ == "__main__":
    game()

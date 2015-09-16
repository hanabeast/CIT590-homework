#Cards.py
#Yilun Fu, Jinghong Zhu

import random  # needed for shuffling a Deck

class Card(object):
    #these two dictionaries are used for presenting  the card to the player
    rank_dic = {'A':'Ace','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','J':'Joker','Q':'Queen','K':'King'}
    suit_dic = {'C':'Club','S':'Spade','H':'Heart','D':'Diamond'}
    
    def __init__(self, rank, suit):
        '''Initialize the card'''
        for rank_element in self.rank_dic.keys():
            if rank.upper() == rank_element:
                rank = rank_element
        for suit_element in self.suit_dic.keys():
            if suit.upper() == suit_element:
                suit = suit_element
        self.rank = rank
        self.suit = suit


    def __str__(self):
        '''This is for represent the card in the tableau'''
        return str(self.rank)+str(self.suit)

    def print_card(self):
        '''This is for present the card to the player'''
        return str(Card.rank_dic[self.rank])+' of '+str(Card.suit_dic[self.suit])

    def get_rank(self):
        '''Get the rank'''
        return self.rank

    def get_suit(self):
        '''Get the suit'''
        return self.suit

    def get_value(self):
        if self.get_rank() in ['2','3','4','5','6','7','8','9','10']:
            value = int(self.get_rank())
        elif self.get_rank() in ['J','Q','K']:
            value = 10
        elif self.get_rank() in ['A']:
            value = 1
        return value

class Deck():
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        self.__deck = []
        for rank in Card.rank_dic.keys():
            for suit in Card.suit_dic.keys():
                self.card = Card(rank,suit)
                self.__deck.append(self.card)

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        '''Get the deck'''
        return self.__deck

    def deal(self):
        '''Return the top of the deck '''
        return self.__deck.pop()
        
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
        card_string = ''
        for self.card in self.__deck:
            card_string += str(self.card) + '\n'
        return card_string
 


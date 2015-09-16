#CardsTest.py
#Yilun Fu, Jinghong Zhu

from Cards import *
import unittest

class TestCards(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('a','c')
        self.card2 = Card('3','S')
        self.card3 = Card('J','h')
        self.deck = Deck()

    def test_card_get_rank(self):
        self.assertEqual(self.card1.get_rank(),'A',"check card1's rank -> 'A'")
        self.assertEqual(self.card2.get_rank(),'3',"check card2's rank -> '3'")
        self.assertEqual(self.card3.get_rank(),'J',"check card3's rank -> 'J'")

    def test_card_get_suit(self):
        self.assertEqual(self.card1.get_suit(),'C',"check card1's suit -> 'C'")
        self.assertEqual(self.card2.get_suit(),'S',"check card2's suit -> 'S'")
        self.assertEqual(self.card3.get_suit(),'H',"check card3's suit -> 'H'")

    def test_card_init(self):
        self.assertEqual(self.card1.get_rank(),self.card1.rank,"check if card1 is initialized correctly")
        self.assertEqual(self.card1.get_suit(),self.card1.suit,"check if card1 is initialized correctly")
        self.assertEqual(self.card2.get_rank(),self.card2.rank,"check if card1 is initialized correctly")
        self.assertEqual(self.card2.get_suit(),self.card2.suit,"check if card1 is initialized correctly")
        self.assertEqual(self.card3.get_rank(),self.card3.rank,"check if card3 is initialized correctly")
        self.assertEqual(self.card3.get_suit(),self.card3.suit,"check if card3 is initialized correctly")

    def test_card_str(self):
        self.assertEqual(str(self.card1),"AC","check if it prints the right thing")
        self.assertEqual(str(self.card2),"3S","check if it prints the right thing")
        self.assertEqual(str(self.card3),"JH","check if it prints the right thing")

    def test_print_card(self):
        self.assertEqual(self.card1.print_card(),"Ace of Club","check if it prints the right thing")
        self.assertEqual(self.card2.print_card(),"3 of Spade","check if it prints the right thing")
        self.assertEqual(self.card3.print_card(),"Joker of Heart","check if it prints the right thing")

    def test_card_get_value(self):
        value = self.card1.get_value()
        self.assertEqual(value,1,"check if 'A' -> 1")
        value = self.card2.get_value()
        self.assertEqual(value,3,"check if '3' -> 3")
        value = self.card3.get_value()
        self.assertEqual(value,10,"check if 'J' -> 10")
        

##    def test_dect_get_deck(self):
##        self.assertTrue(Card('A','C') in self.deck.get_deck()),"check if the function works fine")

    def test_deck_init(self):
        self.assertEqual(len(self.deck.get_deck()),52,"check if the deck has 52 cards")
        self.assertTrue(str(Card('A','C')) in str(self.deck),"check if ace of club is in deck")
        self.assertTrue(str(Card('8','s')) in str(self.deck),"check if 8 of spade is in deck")
        self.assertTrue(str(Card('j','D')) in str(self.deck),"check if joker of diamond is in deck")
        self.assertTrue(str(Card('2','H')) in str(self.deck),"check if 2 of heart is in deck")
        self.assertTrue(str(Card('9','G')) not in str(self.deck),"check if deck has no such card")
        self.assertTrue(str(Card('11','S')) not in str(self.deck),"check if deck has no such card")

    def test_deck_str(self):
        self.assertEqual(len(str(self.deck)),160,"the length of self.deck should be 51*len('AH')+4*len('10H')+52*len('\n')=160")
        self.assertTrue('AC' in str(self.deck),"check if ace of club is in str")
        self.assertTrue('8S' in str(self.deck),"check if 8 of spade is in str")
        self.assertTrue('JD' in str(self.deck),"check if joker of diamond is in str")
        self.assertTrue('2H' in str(self.deck),"check if 2 of heart is in str")
        self.assertTrue('9G' not in str(self.deck),"check if str has no such card")
        self.assertTrue('11S' not in str(self.deck),"check if str has no such card")
        
    def test_deck_deal(self):
        card = self.deck.deal()
        self.assertEqual(str(card),str(Card('8','D')),"check the top fo the pile is 8 of Dimond")
        self.assertTrue(str(card) not in str(self.deck),"check if the top of piles has been removed")
        self.assertEqual(len(self.deck.get_deck()),51,'check if there is 51 cards left')
        card = self.deck.deal()
        self.assertEqual(str(card),str(Card('8','s')),"check the top fo the pile is 8 of spade")
        self.assertTrue(str(card) not in str(self.deck),"check if the top of piles has been removed")
        self.assertEqual(len(self.deck.get_deck()),50,'check if there is 50 cards left')
        
        
unittest.main()

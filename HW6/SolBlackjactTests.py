#SoloBlackjackTest.py
#Yilun Fu,Jinghong Zhu
from SoloBlackjack import *
from Cards import*
import unittest

class TestSoloBlackjack(unittest.TestCase):
    def setUp(self):
        self.state1 = BlackJack()
        self.state2 = BlackJack()
        self.state2.change_state({'row1':[Card('A','C'),Card('2','D'),Card('3','D'),Card('4','C'),Card('A','D')],'row2':[Card('K','H'),Card('J','C'),Card('J','D'),Card('Q','H'),Card('3','C')],
                       'row3':[Card('7','S'),Card('8','H'),Card('9','S')],'row4':[Card('6','S'),Card('8','D'),Card('9','C')]},[Card('2','H'),Card('2','D'),Card('2','S'),Card('A','S')])
        self.state3 = BlackJack()
        self.state3.change_state({'row1':[Card('10','C'),Card('2','C'),Card('3','D'),Card('4','C'),Card('A','C')],'row2':[Card('K','H'),Card('J','C'),Card('J','D'),Card('Q','H'),Card('3','C')],
                       'row3':[Card('7','S'),Card('8','H'),Card('9','S')],'row4':[Card('6','S'),Card('8','D'),Card('9','C')]},[Card('2','H'),Card('2','D'),Card('2','S'),20])


    def test_init(self):
        self.assertEqual(self.state1.table, {'row1':[1,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]}, 'check if the function works well')
        self.assertEqual(self.state1.discardList, [17,18,19,20], 'check if the function works well')
  
    def test_change_state(self):
        self.assertEqual(str(self.state2.get_table()['row1'][0]), str(Card('A','C')), 'check if table in state2 has been changed')
        self.assertEqual(str(self.state2.get_discard_list()[0]), str(Card('2','H')), 'check if discard list in state2 has been changed')
        self.assertEqual(str(self.state3.get_table()['row2'][0]), str(Card('K','H')), 'check if table in state3 has been changed')
        self.assertEqual(str(self.state3.get_discard_list()[2]), str(Card('2','S')), 'check if discard list in state3 has been changed')


    def test_get_table(self):
        self.assertEqual(self.state1.get_table(), self.state1.table, 'check if the function works well')
        self.assertEqual(self.state2.get_table(), self.state2.table, 'check if the function works well')
        self.assertEqual(self.state3.get_table(), self.state3.table, 'check if the funciton works well')

    def test_get_discard_list(self):
        self.assertEqual(self.state1.get_discard_list(), self.state1.discardList, 'check if the function works well')
        self.assertEqual(self.state2.get_discard_list(), self.state2.discardList, 'check if the function works well')
        self.assertEqual(self.state3.get_discard_list(), self.state3.discardList, 'check if the function works well')

    def test_place_card(self):
        self.assertTrue(self.state1.place_card(Card('A','C'), 1), 'check if this position can be placed')
        self.assertEqual(str(self.state1.get_table()['row1'][0]), str(Card('A','C')), 'check if this card has been placed')
        self.assertFalse(self.state2.place_card(Card('3','S'), 16), 'check whether it will return false if the position has been already taken by card')
        self.assertEqual(str(self.state2.get_table()['row4'][2]), str(Card('9','C')), 'check if this card has not been replaced by other card')
        self.assertFalse(self.state3.place_card(Card('3','S'), 1), 'check whether it will return false if the position has been already taken by card')
        self.assertEqual(str(self.state3.get_table()['row1'][0]), str(Card('10','C')), 'check if this card has not been replaced by other card')
        

    def test_discard_card(self):
        self.state1.discard_card(Card('9','C'))
        self.assertEqual(str(self.state1.get_discard_list()[0]), str(Card('9','C')), 'check if the card has been placed into discard pile')
        self.state3.discard_card(Card('A','C'))
        self.assertEqual(str(self.state3.get_discard_list()[3]), str(Card('A','C')), 'check if the card has been placed into discard pile')
        self.state2.discard_card(Card('10','C'))
        self.assertTrue(Card('10','C') not in self.state2.get_discard_list(), 'check if the card has not been placed into discard pile')

    def test_is_discard_full(self):
        self.assertEqual(self.state1.is_discard_full(), (False, 'nothing'), 'check the discard pile in state 1 is not full')
        self.assertEqual(self.state3.is_discard_full(), (False, 'nothing'), 'check the discard pile in state 3 is not full')
        self.assertEqual(self.state2.is_discard_full(), (True, 'The discard pile is full, you can not discard card'), 'check the discard pile in state 2 is full')
                        
    def test_print_table_line(self):
        print_string = self.state1.print_table_line(self.state1.get_table()['row1'])
        self.assertEqual(print_string,'[  1  ][  2  ][  3  ][  4  ][  5  ]','check if the function works right')
        print_string = self.state2.print_table_line(self.state2.get_discard_list())
        self.assertEqual(print_string,'[  2H ][  2D ][  2S ][  AS ]','check if the function works right')
        print_string = self.state3.print_table_line(self.state3.get_discard_list())
        self.assertEqual(print_string,'[  2H ][  2D ][  2S ][  20 ]','check if the function works right')

    def test_game_not_over(self):
        self.assertTrue(self.state1.game_not_over(),'check state1 is not over because rows in table1 are not full')
        self.assertFalse(self.state2.game_not_over(),'check state2 is over because rows in table2 are full')
        self.assertFalse(self.state3.game_not_over(),'check state3 is over because rows in table3 are full')        

    def test_sum_value(self):
        self.assertEqual(self.state1.sum_value([Card('A','S'),Card('K','S')]),21,'check if A is counted as 11 and K is counted as 10')
        self.assertEqual(self.state1.sum_value([Card('A','S'),Card('K','S'),Card('J','S')]),21,'check if A is counted as 1')
        self.assertEqual(self.state1.sum_value([Card('A','S'),Card('2','S')]),13,'check if A is counted as 11 and 2 is counted as 2')
        self.assertEqual(self.state1.sum_value([Card('4','S'),Card('J','S')]),14,'check if J is counted as 10 and 4 is counted as 4')

    def test_count_points_list(self):
        self.assertEqual(self.state1.count_points_list([Card('A','S'),Card('K','S')]),10,'check if BlackJack gives 10 point')
        self.assertEqual(self.state1.count_points_list([Card('A','S'),Card('K','S'),Card('J','S')]),7,'check if Sum=21(not BlackJack) gives 7 point')        
        self.assertEqual(self.state1.count_points_list([Card('J','S'),Card('K','S')]),5,'check if Sum=20 gives 5 point')
        self.assertEqual(self.state1.count_points_list([Card('9','S'),Card('K','S')]),4,'check if Sum=19 gives 4 point')
        self.assertEqual(self.state1.count_points_list([Card('8','S'),Card('K','S')]),3,'check if Sum=18 gives 3 point')
        self.assertEqual(self.state1.count_points_list([Card('7','S'),Card('K','S')]),2,'check if Sum=17 gives 2 point')
        self.assertEqual(self.state1.count_points_list([Card('6','S'),Card('K','S')]),1,'check if Sum=16 gives 1 point')
        self.assertEqual(self.state1.count_points_list([Card('2','S'),Card('K','S')]),1,'check if Sum<16 gives 1 point')
        self.assertEqual(self.state1.count_points_list([Card('7','S'),Card('K','S'),Card('J','S')]),0,'check if BUST gives 0 point')

    def test_count_total_points(self):
        self.assertEqual(self.state2.count_total_points(),18,'check total points of table 2 is 18')
        self.assertEqual(self.state3.count_total_points(),11,'check total points of table 3 is 11')

    def test_compare_point(self):
        self.assertTrue(self.state1.compare_point(11, 15),'check if the function works fine')
        self.assertFalse(self.state1.compare_point(27, 20),'check if the function works fine')
        self.assertFalse(self.state1.compare_point(13, 13),'check if the function works fine')

    def test_check_position(self):
        self.assertEqual(self.state2.check_position(Card('A','C'),'jk'),(False, 'Ooops, invalid input'),'check if position is not valid')
        self.assertEqual(self.state2.check_position(Card('A','C'),'1.2'),(False, 'Ooops, invalid input'),'check if position is not valid')
        self.assertEqual(self.state2.check_position(Card('A','C'),'18'),(False, 'Ooops, this position belongs to the discard plie'),'check if position belongs to the discard pile')       
        self.assertEqual(self.state2.check_position(Card('A','C'),'-1'),(False, "Ooops, this position doesn't exist"),"check if position doesn't exist")
        self.assertEqual(self.state2.check_position(Card('A','C'),'1'),(False, 'Ooops, this postion has been already taken'),"check if position has been taken")
        self.assertEqual(self.state1.check_position(Card('A','C'),'1'),(True, 'nothing'),"check if position is available")
 
unittest.main()    






















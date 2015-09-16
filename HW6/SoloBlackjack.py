#SoloBlackjack.py
#Yilun Fu, Jinghong Zhu
#Please set the font to be Courier.

from Cards import *
class BlackJack():
    '''this is for play black jack game'''
    yes_list = ['Y','y','yes','Yes','YES'] #this is for checking choice
    no_list = ['N','n','NO','No','no']  #this is for checking choice
    def __init__(self):
        self.table = {}
        self.table['row1'] = [1,2,3,4,5]
        self.table['row2'] = [6,7,8,9,10]
        self.table['row3'] = [11,12,13]
        self.table['row4'] = [14,15,16]
        self.discardList = [17,18,19,20]

# unit test functions
    def get_table(self):
        '''get the table'''
        return self.table

    def get_discard_list(self):
        '''get the discard list'''
        return self.discardList

    def change_state(self, newTable,newList):
        '''change the table and discardList'''
        self.table = newTable
        self.discardList = newList

        

# game play helper functions
    def place_card(self, card, position):
        '''place card at the right place'''
        for row in self.table.keys():
            for element in self.table[row]:
                if element == position:
                    index = self.table[row].index(element)
                    self.table[row][index] = card
                    return True
        return False


    def discard_card(self, card):
        '''discard card'''
        for element in self.discardList:
            if type(element) == int:
                index = self.discardList.index(element)
                self.discardList[index] = card
                break

    def is_discard_full(self):
        '''check if the discard is full'''
        for element in self.discardList:
            if type(element) == int:
                return (False,'nothing')  #fisrt element is a boolean, second element is a string to be printed.if it's nothing, then we don't have to print anything
        return (True, 'The discard pile is full, you can not discard card')  #first element is a boolean, second element is a string to be printed.

    def print_table_line(self,alist):
        '''enter a list, edit it to as string'''
        print_string=''
        for element in alist:
            if len(str(element)) == 3:
                print_string += '[ '+str(element)+' ]'
            if len(str(element)) == 1:
                print_string += '[  '+str(element)+'  ]'
            if len(str(element)) == 2:
                print_string += '[  '+str(element)+' ]'
        return print_string

    def game_not_over(self):
        '''as a signal to decide whether game ends'''
        for row in self.table.keys():
            for element in self.table[row]:
                if type(element) == int:
                    return True
        return False

    def display_state(self):   #No unit test required
         '''display the table'''
         print '\nThe table is:\n'
         for row in self.table.keys():
            print_string=''
            if len(self.table[row]) == 5:
                print_string = self.print_table_line(self.table[row])
            if len(self.table[row]) == 3:
                print_string = 7*' '+self.print_table_line(self.table[row])
            print print_string 
         print '\nThe dicard pile is:\n'
         print_string = self.print_table_line(self.discardList)
         print print_string

         
# count score funtions
    def sum_value(self, alist):
        '''sum the value of a card list'''
        value_list = []
        for card in alist:
            value = card.get_value()
            value_list.append(value)
        sum_of_list = sum(value_list)
        if sum_of_list <= 11 and 1 in value_list:          #to check if ace could be counted as 11
            sum_of_list += 10
        return sum_of_list
        

    def count_points_list(self, alist):
        '''count points of one list'''
        if self.sum_value(alist) == 21:
            if len(alist) == 2:
                points = 10
            else:
                points = 7
        elif self.sum_value(alist) == 20:
            points = 5
        elif self.sum_value(alist) == 19:
            points = 4
        elif self.sum_value(alist) == 18:
            points = 3
        elif self.sum_value(alist) == 17:
            points = 2
        elif self.sum_value(alist) <= 16:
            points = 1
        else:
            points = 0
        return points

    def count_total_points(self):
        '''count total point'''
        row1_score = self.count_points_list(self.table['row1'])
        row2_score = self.count_points_list(self.table['row2'])
        row3_score = self.count_points_list(self.table['row3'])
        row4_score = self.count_points_list(self.table['row4'])
        column1_score = self.count_points_list([self.table['row1'][0],self.table['row2'][0]])
        column2_score = self.count_points_list([self.table['row1'][1],self.table['row2'][1],self.table['row3'][0],self.table['row4'][0]])
        column3_score = self.count_points_list([self.table['row1'][2],self.table['row2'][2],self.table['row3'][1],self.table['row4'][1]])
        column4_score = self.count_points_list([self.table['row1'][3],self.table['row2'][3],self.table['row3'][2],self.table['row4'][2]])
        column5_score = self.count_points_list([self.table['row1'][4],self.table['row2'][4]])
        total_score = sum([row1_score,row2_score,row3_score,row4_score,column1_score,column2_score,column3_score,column4_score,column5_score])
        return total_score

#point comparing funtion
    def compare_point(self, current_point, point):
        '''Compare the point to the point in the file and if point is bigger, rewrite the file'''
        if point>current_point:
            return True
        return False


#error checking functions
    def check_position(self, card, position):
        '''Check the position input'''
        try:
            position = float(position)
        except:
            return (False, 'Ooops, invalid input')  #fisrt element is a boolean, second element is a string to be printed.
        if position != int(position):
            return (False, 'Ooops, invalid input')  #fisrt element is a boolean, second element is a string to be printed.
        elif position in range (17,21):
            return (False, 'Ooops, this position belongs to the discard plie')  #fisrt element is a boolean, second element is a string to be printed.
        elif position not in range (1,17):
            return (False, "Ooops, this position doesn't exist")  #fisrt element is a boolean, second element is a string to be printed.
        elif self.place_card(card, position) == False:
            return (False, 'Ooops, this postion has been already taken')  #fisrt element is a boolean, second element is a string to be printed.
        return (True,'nothing') #fisrt element is a boolean, second element is a string to be printed.if it's nothing, then we don't have to print anything

    def check_choice(self, choice):  #here, choice is a string
        '''Check the choice input'''
        if choice in self.yes_list+self.no_list:
            return True
        print 'Ooops, invalid input'
        return False

#to simplify the play function (these function needs some input, so no unit test required)
    def ask_for_position(self, card):  
        '''Ask for the postion to replace and replace the card'''
        position = raw_input('Choose the position you want to replace: ')
        while self.check_position(card, position)[0] == False:
            print self.check_position(card, position)[1]
            position = raw_input('Choose the position you want to replace: ')

    def middle_step(self):
        '''This is for playing the game till game is over'''
        deck = Deck()
        deck.shuffle()
        while self.game_not_over():
            self.display_state()
            card = deck.deal()
            print '\nthe card you get from the deck is '+card.print_card()
            if self.is_discard_full()[0] == False:
                choice1 = raw_input('Do you want to put it in discard:(press y or n)')
                while self.check_choice(choice1) != True:
                    choice1 = raw_input('Do you want to put it in discard:(press y or n)')
                if choice1 in self.yes_list:
                    self.discard_card(card)
                else:
                    self.ask_for_position(card)
            else:
                print self.is_discard_full()[1]
                self.ask_for_position(card)            

    def final_step(self):
        '''while game is over, this is for the final step'''
        print '\nCalculating points you get...'
        print 'Your final state is:\n'
        self.display_state()
        point = self.count_total_points()
        fo = open('highScore.txt')
        current_point = int(fo.readline())
        fo.close()
        if self.compare_point(current_point, point):
            print 'Congratulations, you break the record'
            fo = open('highScore.txt','w')
            fo.write(str(point))
            fo.close()
        print 'Your final score is '+str(point)
        choice2 = raw_input('Game is over. Do you want to restart?(press y or n)')
        while self.check_choice(choice2) != True:
            choice2 = raw_input('Game is over. Do you want to restart?(press y or n)')
        if choice2 in self.yes_list:
            BlackJack().play()
                                             
                
        
#play funtion
    def play(self):
        ''' for playing the game'''
        print '''\nWelcome to Solo Black Jack game\n'''
        print '''The game is a solo game, so in that sense it is like solitaire, but all of the scoring comes from blackjack.In blackjack a hands score should stay at or below a value of 21.\n
In this game, blackjack hands are scored from ninehands formed byeach of the four rows and five columns of the grid of cards laid out. To play the game you draw cardsone at a time from the deck and place them on the grid.\n
Once placed, a card cannot be moved. The four discard spotsallow one to ignore four cards by placing them in the discard spots rather than on the grid. Once all sixteen spots in the grid have cards, game is over and a score is calculated.\n'''
        print '''\nThe score rule is:
Hand                Points                    Explanation
<BJ>                10                        two cards that total 21
<21>                 7                        3, 4 or 5 cards total 21
<20>                 5                        Hands total 20
<19>                 4                        Hands total 19
<18>                 3                        Hands total 18
<17>                 2                        Hands total 17
<=16                 1                        Hands total 16 or less
>=22                 0                        Hands total 22 or more

'''
        print '''To simplify the display of cards in the table and discard list, we use a number to represen a blank spot and a card number and a suit to represent that particular spot being used by that particular card.For example, number 13 represents a blank position 13 and QH present Queen of Heart, where the suit S, H, C, D represents Spade, Heart, Club, Dimond.'''
        self.middle_step()
        self.final_step()
                                             
def main():
    bj_solitaire = BlackJack()
    bj_solitaire.play()


if __name__ == '__main__':
    main()
        
        

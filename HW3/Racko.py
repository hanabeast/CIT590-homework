#Racko.py
#Yilun Fu, Kuo-Hao Chen
import string
import random
global deck
global discard
deck=range(1,61)
discard=[]

def shuffle():
    '''to shuffle the deck or the discard pile'''
    global deck
    global discard
    if len(deck)==0:
        random.shuffle(discard)
    else:
        random.shuffle(deck)
        
def check_racko(rack):
    '''check if Racko has been achieved'''
    return rack==sorted(rack,reverse=True)

def deal_card():
    '''get the top card from the deck'''
    global deck
    return deck.pop()

def deal_initial_hands():
    '''return user's hand and computer's hand'''
    human_hand=[]
    computer_hand=[]
    for i in range(0,10):
        computer_hand.append(deal_card())
        human_hand.append(deal_card())
    return (human_hand,computer_hand)
    
def does_user_begin():
    '''decide who goes first by simulating a coin toss'''
    coinRandomNum=random.randint(0,1)
    return coinRandomNum==0
    

def print_top_to_bottom(rack):
    '''give a rack, print it out from top to bottom'''
    for card in rack:
        print card

def find_and_replace(newCard,cardToBeReplaced,hand):
    '''find the card to be replaced and replace it with new card'''
    global discard
    while cardToBeReplaced not in hand:
        print 'Sorry, you should choose card in your hand,try again'
        cardToBeReplaced=input('Input the number in your card to be replaced:')
    for i in range(0,10):
        if hand[i]==cardToBeReplaced:
            index=i
    hand[index]=newCard
    add_card_to_discard(cardToBeReplaced)
    return hand

def add_card_to_discard(card):
    '''add the card to the top of the dicard pile'''
    discard.append(card)

def computer_strategy(a,b,card,hand):
    '''decide how computer should move after seeing the card'''
    '''we do it by devide the 10 slots to 5 pairs, in which the first pair only accepts
numbers from 1 to 12 and so on. We set the lowest boundary=a and the highest boundary
=b-1 in each pair.Then we first decide which slot should we put the card
in, and then the index of the pairs in the slots is i an j. The fisrt card in such pair is
hand[i], and the second card in such pair is hand[j].Then we make some decision'''
    global deck
    global discard
    if card in range(a,b+1):
        c=(a+b)/2.0                                #find the mean of a and b
        i=(55-a)/6                                   #find the index of last slot
        j=(60-b)/6                                   #find the index of secondlast slot
        if hand[i] in range(a,b+1) and hand[j] in range(a,b+1) and hand[i]<hand[j]:
            return False
        if (hand[i]>c or hand[i]<a) and card<c:
            find_and_replace(card,hand[i],hand)
            return True
        if (hand[j]<c or hand[j]>b) and card>c:
            find_and_replace(card,hand[j],hand)
            return True
        if hand[i] in range(a,b+1) and card>hand[i]:
            find_and_replace(card,hand[j],hand)
            return True
        if hand[j] in range(a,b+1) and card<hand[j]:
            find_and_replace(card,hand[i],hand)
            return True
    return False
        
def computer_play(hand):
    '''write down the computer strategy'''
    global deck
    global discard
    card=discard.pop()
    if computer_strategy(1,12,card,hand) or computer_strategy(13,24,card,hand) or computer_strategy(25,36,card,hand) or computer_strategy(37,48,card,hand) or computer_strategy(49,60,card,hand):
        True     # we don't have to do anything if computer_strategy returns true, so just put something meaningless here.
    else:
        add_card_to_discard(card)
        card=deal_card()
        if computer_strategy(1,12,card,hand) or computer_strategy(13,24,card,hand) or computer_strategy(25,36,card,hand) or computer_strategy(37,48,card,hand) or computer_strategy(49,60,card,hand):
            True  # we don't have to do anything if computer_strategy returns true, so just put something meaningless here.
        else:
            add_card_to_discard(card)
    #print hand         this is for test
    return hand

def human_play(hand):
    '''write down how the human plays this game'''
    global deck
    global discard
    print_top_to_bottom(hand)
    card=discard.pop()
    print 'The card you get from the discard is '+str(card)
    choice=raw_input('Do you want to keep this card?Please enter y or n:')
    while choice not in ['y','Y','n','N']:
        print 'Error,Please enter y or n or just press enter as yes:'
        choice=raw_input('Do you want to keep this card?Please enter y or n:')
    if choice in ['y','Y']:
        cardToBeReplaced=input('Input the number in your card to be replaced:')
        hand=find_and_replace(card,cardToBeReplaced,hand)
    else:
        add_card_to_discard(card)
        card=deal_card()
        print 'The card you get from the deck is ' +str(card)
        secondChoice=raw_input('Do you want to keep this card?Please enter y or n:')
        while secondChoice not in ['y','Y','n','N']:
            print 'Error,Please enter y or n or just press enter as yes:'
            secondChoice=raw_input('Do you want to keep this card?Please enter y or n:')
        if secondChoice in ['y','Y']:
            cardToBeReplaced=input('Input the number in your card to be replaced:')
            hand=find_and_replace(card,cardToBeReplaced,hand)
        else:
            add_card_to_discard(card)
    return hand

def reStart():
    '''when len(deck)=0, get to restart'''
    global deck
    global discard
    print 'Oh, the deck runs out, we have to shuffle the discard and put them as deck.'
    shuffle()
    (deck,discard)=(discard,deck)
    card=deal_card()
    add_card_to_discard(card)
            
            
def main():
    global deck
    global discard
    shuffle()
    (human_hand,computer_hand)=deal_initial_hands()
    card=deal_card()
    add_card_to_discard(card)
    userStarts=does_user_begin()
    #print discard        this is for test
    if userStarts:
        print 'the coin toss is head, user goes first'
        while check_racko(human_hand)==False and check_racko(computer_hand)==False:
            human_hand=human_play(human_hand)
            if len(deck)==0:
                reStart()
            if check_racko(human_hand)==True:
                break
            computer_hand=computer_play(computer_hand)
            if len(deck)==0:
                reStart()
            #print discard        this is for test
    else:
        print 'the coin toss is tail, computer goes first'
        while check_racko(human_hand)==False and check_racko(computer_hand)==False:
            computer_hand=computer_play(computer_hand)
            if len(deck)==0:
                reStart()
            if check_racko(computer_hand)==True:
                break
            human_hand=human_play(human_hand)
            if len(deck)==0:
                reStart()
            #print discard       this is for test
    if check_racko(human_hand)==True:
        print "Congratulations! You beat the computer"
    if check_racko(computer_hand)==True:
        print "O, the computer beat you. Don't be frustrated, you can start again"

if __name__=='__main__':
    main()
        

    
        

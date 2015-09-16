#HW7.py
import csv

def sameAB(string):
    ''' check if an input string is of the form aaaa...abbbb...b'''
    if not string:
        return True
    if string[0] != 'a' or string[-1] != 'b':
        return False
    else:
        return sameAB(string[1:-1])

def binary_search(lst, val):
    ''' check if a val is in the list '''
    if not lst:
        return False
    mid = len(lst)/2
    left = lst[:mid]
    right = lst[mid+1:]
    if val == lst[mid]:
        return True
    elif val < lst[mid]:
        return binary_search(left, val)
    elif val > lst[mid]:
        return binary_search(right, val)

def flatten(lst):
    ''' flatten a list which contains a collection of lists '''
    if not lst:
        return []
    dummy_lst = []
    for element in lst[0]:
        dummy_lst.append(element)
    return dummy_lst + flatten(lst[1:])


def initials(lst):
    '''create a list of initials of strings being passed in as names'''
    return map(lambda x:x.split()[0][0]+'.'+x.split()[1][0]+'.',lst)

def meamers(filename):
    ''' find the number of students who are from MEAM '''
    fo = open(filename)
    lines = fo.readline().split('\r') # I can't find a better way to reade csv file,tried using the method in hw4 but didn't work
    # I'll attach my csv file 
    lst = [line for line in lines if line.split(',')[1] == 'MEAM']
    print len(lst)
    
    
        

def most_frequent_alphabet(frequency_dictionary):
    '''find the alphabet that is appearing the most times'''
    return [k for k in frequency_dictionary if frequency_dictionary[k] == max(frequency_dictionary.values())]
       
            


\



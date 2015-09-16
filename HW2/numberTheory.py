#numberTheory.py
import math
import string
def isPrime(x):
    '''check whether number x is prime'''
    if x==1:
        return False
    for i in range(2,int(x)):
        if x%i==0:
            return False
    return True

def isComposite(x):
    '''check whether number x is composite'''
    if x==1:
        return False
    elif isPrime(x):
        return False
    return True

def factorsSum(x):
    '''find the sum of all x's factors'''
    sum_of_factors=0
    for i in range(1,int(x)):
            if x%i==0:
               sum_of_factors=sum_of_factors+i
    return sum_of_factors
    
def isPerfect(x):
    '''check whether number x is perfect'''
    return factorsSum(x)==x

def isAbundant(x):
    '''check whether number x is abundant'''
    return factorsSum(x)>x

def isInt(x):
    '''check if x is an integer or not'''
    return x==int(x) and x>0

def checkSolution(a,b,c):
    '''check if a*x^2+b*x+c=0 has integer solutions'''
    if b**2-4*a*c<0:
        return False
    else:
        delta=math.sqrt(b**2-4*a*c)
        solution_a=(-b+delta)/(2*a)
        solution_b=(-b-delta)/(2*a)
    return isInt(solution_a) or isInt(solution_b)

def isTriangular(x):
    '''check if x is triangular'''
    return checkSolution(0.5,0.5,-x)
 
def isPentagonal(x):
    '''check if x is pentagonal'''
    return checkSolution(1.5,-0.5,-x)
    
def isHexagonal(x):
    '''check if x is hexagonal'''
    return checkSolution(2,-1,-x)

def finalprint(x):
    ''' get the finalprint '''
    if isPrime(x):
        finalprint=str(x)+' is prime,'
    else:
        finalprint=str(x)+' is not prime,'
    if isComposite(x):
        finalprint=finalprint+' is composite,'
    else:
        finalprint=finalprint+' is not composite,'
    if isPerfect(x):
        finalprint=finalprint+' is perfect,'
    else:
        finalprint=finalprint+' is not perfect,'
    if isAbundant(x):
        finalprint=finalprint+' is abundant,'
    else:
        finalprint=finalprint+' is not abundant,'
    if isTriangular(x):
        finalprint=finalprint+' is triangular,'
    else:
        finalprint=finalprint+' is not triangular,'
    if isPentagonal(x):
        finalprint=finalprint+' is pentagonal,'
    else:
        finalprint=finalprint+' is not pentagonal,'
    if isHexagonal(x):
        finalprint=finalprint+' is hexagonal.'
    else:
        finalprint=finalprint+' is not hexagonal.'
    print finalprint

def main():
    condition=True
    while condition==True:
        x=input("Please write an integer number between 1 and 10000(if you want to quit,write-1)")
        while (isInt(x)==False or x<0 or x>10000) and x!=-1: #while x!=1 and x doesn't fit the requirement, ask to enter x again
           print "Error,please write an integer number between 1 and 10000(if you want to quit,write-1)"
           x=input("Please write an integer number between 1 and 10000(if you want to quit,write-1)")
        if x==-1:                          #check if x=-1 after the  second loop
            condition=False
        else:
            finalprint(x)

if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    

    
    

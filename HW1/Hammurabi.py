#Harmmurabi.py
import random
def print_intro():
    print '''Congrats, you are the newest ruler of ancient Samaria,elected for a ten year term of office. Your duties are to distribute food, direct farming, and buy and sell land as needed to support your people. Watch out for rat infestations and the resultant plague! Grain is the general currency, measured in bushels. The following will help you in your decisions:

    * Each person needs at least 20 bushels of grain per year to survivie.
    * Each person can farm at most 10 acres of land.
    * It takes 2 bushels of grain to farm an acre of land.
    * The market price for land fluctuates yearly.

    Rule wisely and you will be showered with appreciation at the end of your term. Rule pooly and you will be kicked out of office!'''

def ask_to_buy_land(bushels,cost):
    '''Ask user how many bushels to spend buying land.'''
    acres=input("How many acres will you buy? ")
    while acres*cost>bushels:
        print "O great Hammurabi, we have but",bushels,"bushels of grain!"
        acres=input("How many acres will you buy? ")
    return acres

def ask_to_sell_land(acres):
    '''Ask user how much land they want to sell.'''
    acres_sold=input("How many land will you sell? ")
    while acres_sold>acres:
        print "O great Hammurabi, we have but",acres,"acres of land!"
        acres_sold=input("How many acres will you sell? ")
    return acres_sold
    
def ask_to_feed(bushels):
    '''Ask user how many bushels they want to use for feeding.'''
    bushels_feeding=input("How many bushels will you want to use for feeding?")
    while bushels_feeding>bushels:
        print "O great Hammurabi, we have but",bushels,"bushels of grain!"
        bushels_feeding=input("How many bushels will you want to use for feeding?")
    return bushels_feeding

def ask_to_cultivate(acres,population,bushels):
    '''Ask user how much land they want to plant seed in '''
    acres_plant=input("How many acres of land will you want to plant seed in?")
    while acres_plant>acres:
        print "O great Hammurabi we have but",acres,"acres of land!"
        acres_plant=input("How many acres of land will you want to plant seed in?")
    while acres_plant>bushels/2:
        print "O great Hammurabi, we have but",bushels,"bushels of grain!"
        acres_plant=input("How many acres of land will you want to plant seed in?")
    while acres_plant>10*population:
        print "O great Hammurabi,we have but",population,"people!"
        acres_plant=input("How many acres of land will you want to plant seed in?")
    return acres_plant

def isPlague():
    isplague=random.randint(1,100)
    if isplague<16:
        return True
    else:
        return False
        

def numStarving(population,bushels):
    num_Starving=population-bushels/20
    if num_Starving<0:
        num_Starving=0
    elif num_Starving>0.45*population:
        print "O great Hammurabi,you are kicked out of office because too many people starved!"
        quit()
    return num_Starving       
    
def numImmigrants(land,grainInStorage,population,num_Starving):
    if num_Starving>0:
        num_Immigrants=0
    else:
        num_Immigrants=int((20*land+grainInStorage)/(100*population+1))
    return num_Immigrants

def getHarvest():
    return random.randint(1,8)

def effectOfRats():
    return random.randint(10,30)/100.0

def priceOfLand():
    return random.randint(16,22)

def finalSummary(starved,immigrants,population,harvest,bushels_per_acre,rats_ate,bushels_in_storage,acres_owned,plague_deaths):
    print "O great Hammurabi, you have ruled for 10 years!"
    print "In the previous year",starved,"people starved to death."
    print "In the previous year",immigrants,"people entered the kingdom."
    print "The final population is ",population
    print "We harvested",harvest,"bushels at",bushels_per_acre,"bushels per acre."
    print "Rats detroyed",rats_ate,"bushels,leaving",bushels_in_storage,"bushels in storage."
    print "The city final owns",acres_owned,"acres of land."
    print "There were", plague_deaths,"deaths from the plague."
    if population>100 and acres>1200:
        print "O great Hammurabi,excellent!"
    elif population>50 and acres>800:
        print "O great Hammurabi,you are good!"
    else:
        print "O great Hammurabi,you need improvement!"
    
def Hammurabi():
    starved=0
    immigrants=5
    population=100
    harvest=3000           #total bushels harvested
    bushels_per_acre=3   #amount harvested for each acre planted
    rats_ate=200           #bushels destroyed by rats
    bushels_in_storage=2800
    acres_owned=1000
    cost_per_acre=19      #each acre costs this many bushels
    plague_deaths=0
    print_intro()
    for year in range (1,11):
         print "O great Hammurabi!"
         print "You are in year",year,"of your ten year rule."
         print "In the previous year",starved,"people starved to death."
         print "In the previous year",immigrants,"people entered the kingdom."
         print "The population is now",population
         print "We harvested",harvest,"bushels at",bushels_per_acre,"bushels per acre."
         print "Rats detroyed",rats_ate,"bushels,leaving",bushels_in_storage,"bushels in storage."
         print "The city owns",acres_owned,"acres of land."
         print "Land is currently worth",cost_per_acre,"bushels per acre."
         print "There were", plague_deaths,"deaths from the plague."
         acres_bought=ask_to_buy_land(bushels_in_storage,cost_per_acre)
         if acres_bought==0:
               acres_sold=ask_to_sell_land(acres_owned)
         else:
             acres_sold=0
         acres_owned=acres_owned+acres_bought-acres_sold                       #acres_owned change sbecause of trade
         bushels_in_storage=bushels_in_storage+cost_per_acre*acres_sold-cost_per_acre*acres_bought     
         bushels_feeding=ask_to_feed(bushels_in_storage)                    #ask for feeding
         bushels_in_storage=bushels_in_storage-bushels_feeding             #bushels_in_storage changes again
         acres_plant=ask_to_cultivate(acres_owned,population,bushels_in_storage)
         bushels_in_storage=bushels_in_storage-2*acres_plant               #bushels_in_storage changes again
         ''' calculate the population'''
         if isPlague():                                                           #check if there is a plague
             plague_deaths=int(population*0.5)
         else:
             plague_deaths=0
         starved=numStarving(population,bushels_feeding)               #calculating num_starving
         population=population-plague_deaths-starved                   #calculatint the population before we decide the number of immigrants
         immigrants=numImmigrants(acres_owned,bushels_in_storage,population,starved)
         population=population+immigrants                #calculating final population
         ''' calculate the bushels_in_storage for next year '''
         bushels_per_acre=getHarvest()                                        
         harvest=bushels_per_acre*acres_plant
         bushels_in_storage=bushels_in_storage+harvest
         ''' check if there is a rats infestation '''
         if random.random()<0.4:
             rats_ate=int(effectOfRats()*bushels_in_storage)
         else:
             rat_ate=0
         bushels_in_storage=bushels_in_storage-rats_ate
         cost_per_acre=priceOfLand()                                           #cost of land changes for the next year
    ''' after ten years, now we give a final summary '''       
    finalSummary(starved,immigrants,population,harvest,bushels_per_acre,rats_ate,bushels_in_storage,acres_owned,plague_deaths)
        
             
        
            
 
        
        
              
         

    

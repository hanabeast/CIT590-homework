#movie_trivia.py
#Xu He, Yilun Fu

import csv
def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        movieInfo[actor] = set(movies)
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict

#Utility Functions

def split_list(lst):
    '''split database.values() into a small list'''
    split_list = []
    for element_list in lst:
        for element in element_list:
            split_list.append(element)
    return split_list

def insert_actor_info(actor, movies, movie_Db):
    '''Insert infomation into movie_Db'''
    movie_set = set(movies.split(','))
    if actor not in movie_Db.keys():
        movie_Db[actor] = movie_set
    else:
        movie_Db[actor].update(movie_set)
        
def insert_rating(movie, ratings, ratings_Db):
    '''Insert into/update movie ratings'''
    ratings_Db[movie] = [str(ratings[0]), str(ratings[1])]

        

def delete_movie(movie, movie_Db, ratings_Db):
    '''Delete all information from the database that corresponds to this movie'''
    if movie in ratings_Db.keys():
        del ratings_Db[movie]
    for actor in movie_Db.keys():
        if movie in movie_Db[actor]:
            movie_Db[actor].remove(movie)
    
    

def select_where_actor_is(actorName, movie_Db):
    '''Given an actor,return the list of all movies'''
    if actorName not in movie_Db.keys():
        return ['not present']
    if actorName in movie_Db.keys():
        return list(movie_Db[actorName])

def select_where_movie_is(movieName, movie_Db):
    '''Given a movie,return the list of all actors'''
    actor_list = []
    if movieName not in split_list(movie_Db.values()):
        return ['not present']
    for actor in movie_Db.keys():
        if movieName in movie_Db[actor]:
            actor_list.append(actor)
    return actor_list
            

def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
    '''Return a list of movies that satisfy an inequality of equality
 based on the comparison argument and the targeted rating argument.'''
    movie_list = []
    if comparison == '>':
        if is_critic == True:
            for movie in ratings_Db.keys():
                if int(ratings_Db[movie][0]) > targeted_rating:
                    movie_list.append(movie)
        elif is_critic == False:
            for movie in ratings_Db.keys():
                if int(ratings_Db[movie][1]) > targeted_rating:
                    movie_list.append(movie)
    elif comparison == '<':
        if is_critic == True:
            for movie in ratings_Db.keys():
                if int(ratings_Db[movie][0]) < targeted_rating:
                    movie_list.append(movie)
        elif is_critic == False:
            for movie in ratings_Db.keys():
                if int(ratings_Db[movie][1]) < targeted_rating:
                    movie_list.append(movie)
    elif comparison == '=':
        if is_critic == True:
            for movie in ratings_Db.keys():
                if int(ratings_Db[movie][0]) == targeted_rating:
                    movie_list.append(movie)
        elif is_critic == False:
            for movie in ratings_Db.keys():
                if int(ratings_Db[movie][1]) == targeted_rating:
                    movie_list.append(movie)
    if movie_list == []:
        return ['not present']
    return movie_list

def actor_name_converting(name, moviedb):
    '''Convert actor name into the corresponding name in database'''
    for actor in moviedb.keys():
        if actor.lower() == name.lower():
            name_in_database = actor
            return name_in_database
    return name

def movie_name_converting(name, moviedb):
    '''Convert movie name into the corresponding name in database'''
    for movie in split_list(moviedb.values()):
        if movie.lower() == name.lower():
            name_in_database = movie
            return name_in_database
    return name

#User Functions
                   
def get_co_actors(actorName, moviedb):
    '''Return list of all actors that the actor has ever worked with in any movie'''
    if actorName not in moviedb.keys():
        return ['not present']
    co_actor = []
    actor_worked_movie = moviedb[actorName]
    for movie in actor_worked_movie:
        for actor in moviedb.keys():
            if movie in moviedb[actor] and actor not in co_actor and actor != actorName:
                co_actor.append(actor)
    if co_actor == []:
        return ['no result found']
    return co_actor

def get_common_movie(actor1, actor2, moviedb):
    '''Find the movies where both actors were cast'''
    movie_list = []
    if actor1 not in moviedb.keys() or actor2 not in moviedb.keys():
        return ['not present']
    else:
        for movie in moviedb[actor1]:
            if movie in moviedb[actor2]:
                movie_list.append(movie)
    return movie_list

def get_average_ratings(actor, movie_Db, ratings_Db):
    '''Get the average movie rating for actor'''
    Sum_of_ratings_per_critics = 0
    Sum_of_ratings_per_audience = 0
    count_movie = 0
    if actor not in movie_Db.keys():
        return ('not present','not present')
    for movie in movie_Db[actor]:
        if movie in ratings_Db.keys():
            Sum_of_ratings_per_critics += int(ratings_Db[movie][0])
            Sum_of_ratings_per_audience +=int(ratings_Db[movie][1])
            count_movie += 1
    if count_movie == 0:
        return ('no result found','no result found')
    Average_ratings_per_critics = 1.0 * Sum_of_ratings_per_critics / count_movie
    Average_ratings_per_audience = 1.0 * Sum_of_ratings_per_audience / count_movie
    return (Average_ratings_per_critics, Average_ratings_per_audience)
    
        
def critics_darling(movie_Db, ratings_Db):
    ''' Find the actor whose movies have the highest average rotten tomatoes rating,as per the critics'''
    maxScore = 0
    actor_list = []
    for actor in movie_Db.keys():
        actorScore = get_average_ratings(actor, movie_Db, ratings_Db)[0]
        if type(actorScore) != str:
            if actorScore > maxScore:
                maxScore = actorScore
                actor_list = [actor]
            elif actorScore == maxScore:
                actor_list.append(actor)
    return actor_list
        
    

def audience_darling(movie_Db, ratings_Db):
    ''' Find the actor whose movies have the highest average rotten tomatoes rating,as per the audience'''
    maxScore = 0
    actor_list = []
    for actor in movie_Db.keys():
        actorScore = get_average_ratings(actor, movie_Db, ratings_Db)[1]
        if type(actorScore) != str:
            if actorScore > maxScore:
                maxScore = actorScore
                actor_list = [actor]
            elif actorScore == maxScore:
                actor_list.append(actor)
    return actor_list

def good_movies(ratings_Db):
    ''' Return the set of movies that both critics and the audience have rated above 85'''
    movies_list = []
    for movie in ratings_Db.keys():
        if int(ratings_Db[movie][0]) >= 85 and int(ratings_Db[movie][1]) >= 85:
            movies_list.append(movie)
    return set(movies_list)
    
    
def get_common_actors(movie1, movie2, movies_Db):
    ''' Return a list of actors that acted in both movies '''
    actor_list = []
    if movie1 not in split_list(movies_Db.values()) or movie2 not in split_list(movies_Db.values()):
        return ['not present']
    else:
        for actor in movies_Db.keys():
            if movie1 in movies_Db[actor] and movie2 in movies_Db[actor]:
                actor_list.append(actor)
        return actor_list

def bacon_recursion(Actor, coActor, baconNumber, movieDb):
    '''A help function for getting bacon number of an actor'''
    stopFlag = False
    for actor in coActor:
        if actor == 'Kevin Bacon':
            stopFlag = True
            return baconNumber+1
    if stopFlag == False:        
        secondCoActorList = []
        for actor1 in coActor:
            secondCoActors = get_co_actors(actor1, movieDb)
            secondCoActorList.extend(secondCoActors)
        secondCoActorList = list(set(secondCoActorList))
        Actor.extend(coActor)
        Actor = list(set(Actor))
        for actor2 in secondCoActorList:
            if actor2 in Actor:
                secondCoActorList.remove(actor2)
        if secondCoActorList == []:
            return 'not connected'
        else:
            return bacon_recursion(Actor, secondCoActorList, baconNumber+1, movieDb)

def get_bacon(actor, movieDb):
    '''Get bacon number of an actor'''
    baconNum = 0
    if actor == 'Kevin Bacon':
        return baconNum
    else:
        coActor = get_co_actors(actor, movieDb)
        if coActor == []:
            return 'not connected'
        else:
            return bacon_recursion([actor], coActor, baconNum, movieDb)
        
def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    print '''Welcome to our movie database
You have options:'''
    while True:
        choice = input('''Press 1 for finding out the top rated actor by critic
Press 2 for finding out the top rated actor by audience
Press 3 for getting average rating of an actor by critic
Press 4 for getting average rating of an actor by audience
Press 5 for getting good movies(movies that both critics and the audience have rated above 85)
Press 6 for getting co-actors of an actor
Press 7 for getting common movie by two actors
Press 8 for getting common actors of two movies
Press 9 for getting Bacon number of an actor
Press 10 for getting the movies list for an actor
Press 11 for getting the actors list for an movie
Press 12 for getting movies list fitting certain conditions
Press 0 for quitting\n''')
        if choice == 0: #quit
            break
        
        elif choice == 1: #Press 1 for finding out the top rated actor by critic
            print 'The top rated actor by critic is(are)', ','.join(critics_darling(actor_DB,ratings_DB)), '\n'
            
        elif choice == 2: #Press 2 for finding out the top rated actor by audience
            print 'The top rated actor by audience is(are)', ','.join(audience_darling(actor_DB,ratings_DB)), '\n'
            
        elif choice == 3: #Press 3 for getting average rating of an actor by critic
            actor = actor_name_converting(raw_input('Enter the name of actor:'), actor_DB)
            critic_score = get_average_ratings(actor, actor_DB, ratings_DB)[0]
            while critic_score == 'no result found' or critic_score=='not present':
                print 'Sorry, either the actor is not in the database or his(her) movies in the database have no ratings'
                actor = actor_name_converting(raw_input('Enter the name of actor:'), actor_DB)
                critic_score = get_average_ratings(actor, actor_DB, ratings_DB)[0]
            print 'The average critic score of', actor, 'is', critic_score, '\n'
            
        elif choice == 4: #Press 4 for getting average rating of an actor by audience
            actor = actor_name_converting(raw_input('Enter the name of actor:'), actor_DB)
            audience_score = get_average_ratings(actor, actor_DB, ratings_DB)[1]
            while audience_score == 'no result found' or audience_score=='not present':
                print 'Sorry, either the actor is not in the database or his(her) movies in the database have no ratings'
                actor = actor_name_converting(raw_input('Enter the name of actor:'), actor_DB)
                audience_score = get_average_ratings(actor, actor_DB,ratings_DB)[1]
            print 'The average critic score of', actor, 'is', audience_score, '\n'
            
        elif choice == 5: #Press 5 for getting good movies(movies that both critics and the audience have rated above 85)
            print 'Goodmovies are:\n', ', '.join(good_movies(ratings_DB)), '\n'
            
        elif choice == 6: #Press 6 for getting co-actors of an actor
            actor = actor_name_converting(raw_input('Enter the name of actor:'), actor_DB)
            actor_list = get_co_actors(actor, actor_DB)
            while actor_list == ['not present']:
                print 'Sorry,', actor ,'is not in the database'
                actor = actor_name_converting(raw_input('Enter the name of actor:'), actor_DB)
                actor_list = get_co_actors(actor, actor_DB)
            if actor_list == ['no result found']:
                print actor, 'has no co-actor in the databse\n'
            else:
                print actor, 'has co-acted with', ', '.join(actor_list), '\n'
                
        elif choice == 7: #Press 7 for getting common movie by two actors
            actor1 = actor_name_converting(raw_input('Enter the name of first actor:'), actor_DB)
            actor2 = actor_name_converting(raw_input('Enter the name of second actor:'), actor_DB)
            movie_list = get_common_movie(actor1, actor2, actor_DB)
            while actor1 == actor2 and movie_list != ['not present']:
                print 'Ooops,you entered the same name here'
                actor2 = actor_name_converting(raw_input('Please enter another name for second actor:'), actor_DB)
                movie_list = get_common_movie(actor1, actor2, actor_DB)
            while movie_list == ['not present']:
                if actor1 not in actor_DB.keys() and actor2 not in actor_DB.keys():
                    print 'Sorry', actor1, 'and', actor2, 'are not in the database'
                    actor1 = actor_name_converting(raw_input('Enter the name of first actor:'), actor_DB)
                    actor2 = actor_name_converting(raw_input('Enter the name of second actor:'), actor_DB)
                    movie_list = get_common_movie(actor1, actor2, actor_DB)
                elif actor1 not in actor_DB.keys():
                    print 'Sorry', actor1, 'is not in the database'
                    actor1 = actor_name_converting(raw_input('Enter the name of first actor:'), actor_DB)
                    while actor1 == actor2:
                        print 'Ooops,you entered the same name here'
                        actor1 = actor_name_converting(raw_input('Please enter another name for first actor:'), actor_DB)
                    movie_list = get_common_movie(actor1, actor2, actor_DB)
                elif actor2 not in actor_DB.keys():
                    print 'Sorry', actor2, 'is not in the database'
                    actor2 = actor_name_converting(raw_input('Enter the name of second actor:'), actor_DB)
                    movie_list = get_common_movie(actor1, actor2, actor_DB)
                while actor1 == actor2 and movie_list != ['not present']:
                    print 'Ooops,you entered the same name here'
                    actor2 = actor_name_converting(raw_input('Please enter another name for second actor:'), actor_DB)
                    movie_list = get_common_movie(actor1, actor2, actor_DB)
            if movie_list == []:
                print actor1, 'and', actor2, 'have no common movies\n'
            else:
                print actor1, 'and', actor2, 'have co-worked in', ', '.join(movie_list), '\n'

        elif choice == 8: #Press 8 for getting common actors of two movies
            movie1 = movie_name_converting(raw_input('Enter the name of first movie:'), actor_DB)
            movie2 = movie_name_converting(raw_input('Enter the name of second movie:'), actor_DB)
            actors_list = get_common_actors(movie1, movie2, actor_DB)
            while movie1 == movie2 and actors_list != ['not present']:
                print 'Ooops,you entered the same name here'
                movie2 = movie_name_converting(raw_input('Please enter another name for second movie:'), actor_DB)
                actors_list = get_common_actors(movie1, movie2, actor_DB)
            while actors_list == ['not present']:
                if movie1 not in split_list(actor_DB.values()) and movie2 not in split_list(actor_DB.values()):
                    print 'Sorry', movie1, 'and', movie2, 'are not in the database'
                    movie1 = movie_name_converting(raw_input('Enter the name of first movie:'), actor_DB)
                    movie2 = movie_name_converting(raw_input('Enter the name of second movie:'), actor_DB)
                    actors_list = get_common_actors(movie1, movie2, actor_DB)
                elif movie1 not in split_list(actor_DB.values()):
                    print 'Sorry', movie1, 'is not in the database'
                    movie1 = movie_name_converting(raw_input('Enter the name of first movie:'), actor_DB)
                    while movie1 == movie2:
                        print 'Ooops,you entered the same name here'
                        movie1 = movie_name_converting(raw_input('Please enter another name for first movie:'), actor_DB)
                    actors_list = get_common_actors(movie1, movie2, actor_DB)
                elif movie2 not in split_list(actor_DB.values()):
                    print 'Sorry', movie2, 'is not in the database'
                    movie2 = movie_name_converting(raw_input('Enter the name of second movie:'), actor_DB)
                    actors_list = get_common_actors(movie1, movie2, actor_DB)
                while movie1 == movie2 and actors_list != ['not present']:
                    print 'Ooops,you entered the same name here'
                    movie2 = movie_name_converting(raw_input('Please enter another name for second movie:'), actor_DB)
                    actors_list = get_common_actors(movie1, movie2, actor_DB)
            if actors_list == []:
                print movie1, 'and', movie2, 'have no common actors\n'
            else:
                print ', '.join(actors_list), 'have(has) worked in both', movie1, 'and', movie2, '\n'
            
        elif choice == 9: #Press 9 for getting Bacon number of an actor
            actor = actor_name_converting(raw_input('Please enter the name of antor:'), actor_DB)
            while actor not in actor_DB.keys():
                print 'Sorry', actor, 'is not in the database'
                actor = actor_name_converting(raw_input('Please enter the name of antor:'), actor_DB)
            bacon_num = get_bacon(actor, actor_DB)
            if type(bacon_num) != int:
                print actor, 'is not connected to Kevin Bacon\n'
            else:
                print actor, 'has a bacon number of', bacon_num, '\n'
            
        
        elif choice == 10: #Press 10 for getting the movies list for an actor
            actor = actor_name_converting(raw_input('Please enter the name of actor:'), actor_DB)
            movie_list = select_where_actor_is(actor, actor_DB)
            while movie_list == ['not present']:
                print 'Sorry', actor, 'is not in the database'
                actor = actor_name_converting(raw_input('Please enter the name of actor:'), actor_DB)
                movie_list = select_where_actor_is(actor,actor_DB)
            print actor, 'has acted in', ', '.join(movie_list), '\n'
                                  
        elif choice == 11: #Press 11 for getting the actors list for an movie
            movie = movie_name_converting(raw_input('Please enter the name of movie:'), actor_DB)
            actor_list = select_where_movie_is(movie, actor_DB)
            while actor_list == ['not present']:
                print 'Sorry', movie, 'is not in the database'
                movie = movie_name_converting(raw_input('Please enter the name of movie:'), actor_DB)
                actor_list = select_where_movie_is(movie, actor_DB)
            print ', '.join(actor_list), 'has(have) acted in', movie, '\n'

        elif choice == 12: #Press 12 for getting movies list fitting certain conditions
            critic_or_audience = raw_input('Please enter whether you want to find movies fitting cirtic score(press y) or audience score(press n):')
            while critic_or_audience not in ['Y','y','n','N']:
                print 'Error, please press y or n'
                critic_or_audience = raw_input('Please enter whether you want to find movies fitting cirtic_score(press y) or audience score(press n):')
            if critic_or_audience in ['Y','y']:
                is_critic = True
            else:
                is_critic = False
            comparison = raw_input("Please enter the sign of comparison (press '<', '>' or '=')")
            while comparison not in ['<','>','=']:
                print "Error, please press '<', '>' or '='"
                comparison = raw_input("Please enter the sign of comparison (press '<', '>' or '=')")
            targeted_rating = input('''Please enter your a number between 1 and 100 as targeted rating
(we will search movies fitting comparion sign and targeted rating):''')
            while targeted_rating not in range(1,101):
                print "Error, please enter a number between 1 and 100"
                targeted_rating = input('''Please enter your a number between 1 and 100 as targeted rating
(we will search movies fitting comparion sign and targeted rating):''')
            movie_list = select_where_rating_is(targeted_rating,comparison,is_critic,ratings_DB)
            if movie_list == ['not present']:
                print 'No movie fits your requirement\n'
            else:
                print 'The movies fitting your requirement are:\n', ', '.join(movie_list),'\n'
                                        

        else:
            print 'Ooops,', choice, 'is not in the option list\n'


if __name__ == '__main__':
    main()    
    
    

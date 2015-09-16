#Xu He,Yilun Fu
from movie_trivia import *
import unittest

class TestMovies(unittest.TestCase):

    movieDb = {}
    ratingDb = {}

    def setUp(self):
        self.movieDb = create_actors_DB('my_test_actors.txt')
        self.ratingDb = create_ratings_DB('my_ratings.csv')

    def testselect_where_movie_is(self):
        #write test code here using self.ratingDb and self.movieDb
        actors = select_where_movie_is('Seven',  self.movieDb)
        #make some assertion about these actors
        self.assertEqual(set(actors), set(['Morgan Freeman', 'Brad Pitt']), 'check Seven->Morgan Freeman,Brad Pitt')
        actors = select_where_movie_is('Blablabla', self.movieDb)
        self.assertEqual(actors, ['not present'], 'check Blablabla->no result found')

    def testselect_where_actor_is(self):
        movie = select_where_actor_is('Anthony Hopkins', self.movieDb)
        self.assertEqual(set(movie),set(['The Edge',  'Meet Joe Black',  'Hannibal',  'Proof']), 'check Anthony Hopkins movie list')
        movie = select_where_actor_is('Blablabla', self.movieDb)
        self.assertEqual(movie, ['not present'], 'check Blablabla->no result found')

    def testselect_where_rating_is(self):
        movie_list = select_where_rating_is(101, '=', True, self.ratingDb)
        self.assertEqual(movie_list, ['not present'], 'check if no resulf is found')
        movie_list = select_where_rating_is(12, '=', True, self.ratingDb)
        self.assertEqual(set(movie_list), set(['Original Sin']), 'check critic_score=12')
        movie_list = select_where_rating_is(17, '<', True, self.ratingDb)
        self.assertEqual(set(movie_list), set(['Original Sin','Assassins']), 'check critic_score<12')
        movie_list = select_where_rating_is(99, '>', True, self.ratingDb)
        self.assertEqual(set(movie_list), set(['The Odd Couple', 'Maltese Falcon', 'Rear Window',
                                              'Cool Hand Luke', 'How to Steal a Million', 'Lilies of the Field','All About Eve',
                                              'Rebecca','The Philadelphia Story', 'Kind Hearts and Coronets', 'Mary Poppins',
                                              'The Godfather', 'Singin in the Rain', 'On the Waterfront']), 'check critic_score>100')
        movie_list = select_where_rating_is(100, '=', False, self.ratingDb)
        self.assertEqual(set(movie_list), set(['The Avengers']), 'check audience_score=100')
        movie_list = select_where_rating_is(34, '<', False, self.ratingDb)
        self.assertEqual(set(movie_list), set(['Species','Bounce','Planet of the Apes','Wild Wild West']), 'check audience_score<34')
        movie_list = select_where_rating_is(97, '>', False, self.ratingDb)
        self.assertEqual(set(movie_list), set(['The Avengers', 'Seven', 'Mission Impossible', 'Ted', 'The Godfather']), 'check audience_score>97')

    def testsplit_list(self):
        lst = split_list([[1,2], [3,4]])
        self.assertEqual(lst, [1,2,3,4], 'check [[1,2],[3,4]]->[1,2,3,4]')
        lst = split_list([[1,2,3],[4]])
        self.assertEqual(lst, [1,2,3,4], 'check [[1,2,3],[4]]->[1,2,3,4]')

    def testinsert_actor_info(self):
        insert_actor_info('George Scott', 'The Hustler,The Changeling', self.movieDb)
        movie_list = select_where_actor_is('George Scott', self.movieDb)
        self.assertEqual(self.movieDb['George Scott'], set(movie_list), 'check if the info has been updated')
        insert_actor_info('Bruce Lee', 'The Big Boss,Enter the Dragon', self.movieDb)
        movie_list = select_where_actor_is('Bruce Lee', self.movieDb)
        self.assertEqual(self.movieDb['Bruce Lee'], set(movie_list), 'check if the info has been inserted into')

    def testinsert_rating(self):
        insert_rating('Rambo', (90,87), self.ratingDb)
        self.assertEqual(self.ratingDb['Rambo'], ['90','87'], 'check if the info has been updated')
        insert_rating('The Hustler', (78,87), self.ratingDb)
        self.assertEqual(self.ratingDb['The Hustler'], ['78','87'], 'check if the info has been inserted into')

    def testdelete_movie(self):
        delete_movie('Seven', self.movieDb,self.ratingDb)
        actors = select_where_movie_is('Seven', self.movieDb)
        self.assertEqual(actors, ['not present'], 'check Seven->no result found')
        self.assertFalse('Seven' in self.ratingDb.keys())
        delete_movie('Troy', self.movieDb, self.ratingDb)
        actors = select_where_movie_is('Troy', self.movieDb)
        self.assertEqual(actors, ['not present'], 'check Troy->no result found')
        self.assertFalse('Troy' in self.ratingDb.keys())
        delete_movie('Bla', self.movieDb,self.ratingDb)
        actors = select_where_movie_is('Bla', self.movieDb)
        self.assertEqual(actors, ['not present'], 'check Bla->no result found')
        self.assertFalse('Bla' in self.ratingDb.keys())

    def testactor_name_converting(self):
        actorName = actor_name_converting('TOM haNks', self.movieDb)
        self.assertEqual(actorName, 'Tom Hanks', 'check TOM haNks->Tom Hanks')
        actorName = actor_name_converting('Brad pitt', self.movieDb)
        self.assertEqual(actorName, 'Brad Pitt', 'check Brad pitt->Brad Pitt')

    def testmovie_name_converting(self):
        movieName = movie_name_converting('jfk', self.movieDb)
        self.assertEqual(movieName, 'JFK', 'check jfk->JFK')
        movieName = movie_name_converting('Ben-hur', self.movieDb)
        self.assertEqual(movieName, 'Ben-Hur', 'check Ben-hur->Ben-Hur')

    def testget_co_actors(self):
        co_actor = get_co_actors('Brad Pitt',self.movieDb)
        self.assertEqual(set(co_actor), set(['Morgan Freeman', 'Dustin Hoffman', 'Kevin Bacon', 'Angelina Jolie',
                            'Eric Bana', 'Diane Kruger', 'Anthony Hopkins', 'George Clooney', 'Julia Roberts']), 'check Brad Pitt->lists of co-actor')
        co_actor=get_co_actors('Bla', self.movieDb)
        self.assertEqual(co_actor, ['not present'], 'check if Bla->no result found')
        co_actor=get_co_actors('Bette Davis', self.movieDb)
        self.assertEqual(co_actor, ['no result found'], 'check if Bette Davis->no result found')
        

    def testget_common_movie(self):
        movie_list=get_common_movie('Tom Hanks', 'Meg Ryan', self.movieDb)
        self.assertEqual(set(movie_list), set(["You've Got Mail",'Sleepless in Seattle']), 'check the common movie')
        movie_list=get_common_movie('Bla', 'Meg Ryan', self.movieDb)
        self.assertEqual(movie_list, ['not present'], 'check if one of the actors is not in the database')
        movie_list=get_common_movie('Brad Pitt', 'Meg Ryan', self.movieDb)
        self.assertEqual(movie_list, [], 'check if two actors have no common movie')

    def testget_average_ratings(self):
        ratings = get_average_ratings('George Scott', self.movieDb,self.ratingDb)
        self.assertEqual(ratings, (98.5,94), 'check George Scott->(98.5,94)')
        ratings=get_average_ratings('Joan Fontaine', self.movieDb,self.ratingDb)
        self.assertEqual(ratings, (100,92), 'check Joan Fontaine->(100,92)')
        ratings = get_average_ratings('Bla', self.movieDb,self.ratingDb)
        self.assertEqual(ratings, ('not present','not present'), 'check if Bla is not in the database')
        ratings = get_average_ratings('Michael Jordan', self.movieDb, self.ratingDb)
        self.assertEqual(ratings, ('no result found','no result found'), 'check if none of the actor movie is in the ratingDB')


    def testcritics_darling(self):
        criticsDarling = critics_darling(self.movieDb, self.ratingDb)
        self.assertEqual(criticsDarling, ['Joan Fontaine'], 'check criticsDarling->Joan Fontaine')
        
    def testaudience_darling(self):
        audienceDarling = audience_darling(self.movieDb, self.ratingDb)
        self.assertEqual(audienceDarling, ['Diane Keaton'], 'check audienceDarling ->Diane Keaton')

    def testgood_movies(self):
        movie_list = good_movies(self.ratingDb)
        actual_movie_list = ['JFK', 'Lawrence of Arabia', 'X Men: First Class', 'Mrs. Miniver', 'Unforgiven', 'Dr Strangelove',
                          'Argo', 'Escape From Alcatraz', 'Leaving Las Vegas', 'Ordinary People', 'It Happened One Night',
                          'Ben-Hur', 'Million Dollar Baby', 'Mrs Miniver', 'Maltese Falcon', 'Casablanca', 'The Sixth Sense',
                          'Rear Window', 'Mr Smith Goes To Washington', 'Milk', 'Silver Linings Playbook', 'The Sting',
                          'The Lord of the Rings: The Return of the King', 'Rain Man', 'To Sir With Love', 'Annie Hall', 'Roman Holiday',
                          'Guns of Navarone', 'High Noon', 'Double Indemnity', 'My Fair Lady', 'Dirty Harry', 'How to Steal a Million',
                          'The French Connection', 'Some Like It Hot', 'Field of Dreams', 'Scent of a Woman', 'Lilies of the Field', 'Apollo 13',
                          'The Fighter', 'The Deer Hunter', "What's Eating Gilbert Grape", 'All About Eve', 'Goodfellas', 'Mystic River',
                          'The Last Emperor', 'In the Heat of the Night', 'Patton', 'The Lion In Winter', 'Pulp Fiction', 'The Dark Knight',
                          'No Country for Old Men', 'Dog Day Afternoon', 'Rebecca', 'Sabrina', 'Dial M for Murder', "Schindler's List", 'Big Sleep',
                          'The Odd Couple', 'Gone With The Wind', 'Departed', 'Ted', 'Silence of the Lambs', 'Cool Hand Luke', "You Can't Take It With You",
                          'Mary Poppins', 'As Good As it Gets', 'Good Will Hunting', 'My Cousin Vinny', 'The Apartment', 'For a Few Dollars More', 'Amadeus',
                          'Eternal Sunshine of the Spotless Mind', 'Kramer vs. Kramer', 'The Philadelphia Story', 'Gandhi', 'The Godfather Part II', 'Bourne Ultimatum',
                          'Kind Hearts and Coronets', 'Catch Me If You Can', 'The Departed', 'The Godfather', 'Edward Scissorhands', 'Singin in the Rain',
                          'On the Waterfront', 'To Kill a Mockingbird', 'Superman', 'The Bridge on The River Kwai', 'Sound of Music']
        self.assertEqual(set(movie_list), set(actual_movie_list), 'check good_movie->all movies above 85')
        
    def testget_common_actors(self):
        actor_list = get_common_actors("You've Got Mail", 'Sleepless in Seattle', self.movieDb)
        self.assertEqual(set(actor_list), set(['Tom Hanks','Meg Ryan']), 'check common actors of these two movies')
        actor_list = get_common_actors('Seven', 'Forrest Gump', self.movieDb)
        self.assertEqual(actor_list, [], 'check these two movies have no common actors')
        actor_list = get_common_actors('Bla', 'Seven', self.movieDb)
        self.assertEqual(actor_list, ['not present'], 'check if one of these movies is not in the database')

    def testbacon_recursion(self):
        co_actor = get_co_actors('Brad Pitt', self.movieDb)
        bacon_num = bacon_recursion('Brad Pitt', co_actor, 0, self.movieDb)
        self.assertEqual(bacon_num, 1, 'check Brad Pitt->1')
        

    def testget_bacon(self):
        bacon_num = get_bacon('Johnny Depp', self.movieDb)
        self.assertEqual(bacon_num, 4, 'check Johnny Depp->4')
        bacon_num = get_bacon('Sean Connery', self.movieDb)
        self.assertEqual(bacon_num, 'not connected', 'chck Sean Connery->not connected')

   
unittest.main()

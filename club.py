class Club(object):
    club_counter = 0

    def __init__(self,name,country,league,stadium,founded):
        self.name = name
        self.country = country
        self.league = league
        self.stadium = stadium
        self.founded = founded
        Club.club_counter += 1
        print "Calling Club constructor"

    def display_club(self):
        print "Name: " + self.name
        print "Country: " + self.country
        print "League: " + self.league
        print "Stadium: " + self.stadium
        print "Founded:", self.founded

    @staticmethod
    def display_club_counter():
        print "Number of clubs: ", Club.club_counter


class Person(object):
    def __init__(self):
        self.name = "Person"

    def print_name(self):
        print self.name

class Player(Person):
    def __init__(self,name):
        super(Player, self).__init__(name)
        self.name = "Player"

    def print_name(self):
        print self.name


# method overloading
def multiply(n1,n2=1,n3=1):
    print n1 * n2 * n3

multiply(3,3,3)
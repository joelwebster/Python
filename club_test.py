from club import Club

# create club
c1 = Club("Juventus","Italy","Serie A","Juventus Stadium",1897)
c2 = Club("AC Milan","Italy","Serie A","San Siro Stadium",1899)
c3 = Club("Inter Milan","Italy","Serie A","San Siro Stadium",1908)

# add the clubs to a list
clubs_list = [c1,c2]

# append club to existing list
clubs_list.append(c3)

# print the list
for c in clubs_list:
    c.display_club()

# get the list length
print "List length: ", len(clubs_list)

# print the number of clubs
Club.display_club_counter()
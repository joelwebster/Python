from club import Club

# get user input
c_name = raw_input("Enter club name: ")
c_country = raw_input("Enter country: ")
c_league = raw_input("Enter league: ")
c_stadium = raw_input("Enter stadium: ")
c_founded = raw_input("Enter year founded: ")

# construct object from input
c_user = Club(c_name,c_country,c_league,c_stadium,c_founded)

# print created Club
c_user.display_club()
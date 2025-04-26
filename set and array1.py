# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set,"\n")

#remove a number from a set
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("After removing the first element from the said set:")
print(num_set,"\n")

my_candies = {"chocolate", "lollipop", "gummy bear"}
friend_candies = {"lollipop", "gum", "mint"}

# Find candies both you and your friend have
common_candies = my_candies & friend_candies
print("Candies we both love:", common_candies)

# Combine all candies in your collection
all_candies = my_candies | friend_candies
print("Our combined candy collection:", all_candies)

students_present = {"Alice", "Bob", "Charlie"}
all_students = {"Alice", "Bob", "Charlie", "David", "Eva"}

# Students who are absent
absent_students = all_students - students_present
print("Absent students:", absent_students)

team_avengers = {"Iron Man", "Captain America", "Thor", "Black Widow"}
team_xmen = {"Wolverine", "Storm", "Cyclops", "Black Widow"}

# Find heroes who belong to both teams
shared_heroes = team_avengers.intersection(team_xmen)
print("Heroes on both teams:", shared_heroes)

# Form one giant team
mega_team = team_avengers.union(team_xmen)
print("Mega superhero team:", mega_team)

club_a = {"Tom", "Jerry", "Spike", "Tyke"}
club_b = {"Jerry", "Tyke", "Butch", "Nibbles"}

# Find members who belong to only one club
exclusive_members = club_a.symmetric_difference(club_b)
print("Exclusive club members:", exclusive_members)

















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

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) 
print(union_set)


intersection_set = set2.intersection(set1)  # {3}
print(intersection_set)

difference_set = set2.difference(set1)  # {1, 2}
print(difference_set)




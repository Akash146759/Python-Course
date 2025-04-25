# function to check whether palindrome or not
def palind(r):
	e = len(r) - 1
	s = 0
	while(s<e):
		if(r[s]!=r[e]):
			return False
		s+=1
		e-=1
	return True
r = (10,20,30,50,50,30,20,10)
if(palind(r)):
	print("The Tuple is Flip-Flop")
else:
	print("The Tuple is not Flip-Flop")

def is_palindrome(my_tuple):
    return my_tuple == my_tuple[::-1]  # Reverse the tuple using slicing and compare
test_tuple1 = ('r', 'a', 'c', 'e', 'c', 'a', 'r','a')
print(is_palindrome(test_tuple1))
	
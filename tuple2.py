# function to check whether palindrome or not
def palind(r):
	e = len(r) -1
	s = 0
	while(s<e):
		if(r[s]!=r[e]):
			return False
		s+=1
		e-=1
	return True
r = (10,20,30,30,20,10)
if(palind(r)):
	print("The Tuple is Flip-Flop")
else:
	print("The Tuple is not Flip-Flop")
	
    
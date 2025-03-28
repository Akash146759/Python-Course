n = int(input('enter a range'))

for x in range(n): 
    if x % 2 == 0: 
       print(x, "Iteration : twist")
    elif x == 15:
       pass             
    elif x % 5 == 0:    
       print(x, "Iteration : fizz")    
    elif x % 3 == 0:    
       print(x, "Iteration : buzz")    
    else:               
       print(x)        

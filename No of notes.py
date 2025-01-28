
# Taking total amount as input from user
Amount = 780

cal1 = 780 /  43
cal2 = 780 // 43

print('normal division : ',cal1, 'Floor division', cal2)

# Calculating the number of notes of different denominations
note_100 = Amount//100          #= 780 // 100 = 7 plus remainder will be 80
note_50 = (Amount%100)//50      #= (780 % 100) // 50 = 80 // 50 = 1 plus remainder will be 30
note_10 = ((Amount%100)%50)//10 #= ((780 % 100) % 50) // 10 = (80%50) // 10 = 30 // 10 = 3

print( "notes of 100 rupee" , note_100)
print("notes of 50 rupee" , note_50)
print("notes of 10 rupee" , note_10)



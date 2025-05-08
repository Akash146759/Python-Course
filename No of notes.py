
# Taking total amount as input from user
Amount = int(input('number:'))

# Calculating the number of notes of different denominations
note_100 = Amount//100          #= 180 // 100 = 1 plus remainder will be 80
note_50 = (Amount%100)//50      #= (180 % 100) // 50 = 80 // 50 = 1 plus remainder will be 30
note_10 = ((Amount%100)%50)//10 #= ((180 % 100) % 50) // 10 = (80%50) // 10 = 30 // 10 = 3

print( "notes of 100 rupee" , note_100)
print("notes of 50 rupee" , note_50)
print("notes of 10 rupee" , note_10)



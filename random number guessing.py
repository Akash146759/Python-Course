import random

playing = True
number = random.randint(10, 15)  # Keep this as an integer now

print("I will generate a number from 10 to 15, and you have to guess the number one digit at a time.")

while playing:
    guess = input("Give me your best guess!\n")
    
    # Check if the guess is a number
    if guess.isdigit():
        guess_num = int(guess)
        
        if guess_num == number:
            print("🎉 You win the game!")
            print("The number was", number)
            break
        elif guess_num < number:
            print("🔼 Too low! Try a higher number.\n")
        else:
            print("🔽 Too high! Try a lower number.\n")
    else:
        print("❌ Please enter a valid number.\n")

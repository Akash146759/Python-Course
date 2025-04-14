# Emoji dictionary
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "love": "❤️"
}

# Input from the user
word = input("Enter a mood (happy, sad, angry, love): ").lower()

# Output the emoji
if word in emoji_dict:
    print(f"Emoji for '{word}' is: {emoji_dict[word]}")
else:
    print("Sorry, I don't have an emoji for that mood!")

class StringReverser:
    def __init__(self, text):
        self.text = text
    
    def reverse_words(self):
        words = self.text.split()  # Split the string into words
        reversed_words = words[::-1]  # Reverse the word order
        return " ".join(reversed_words)  # Join the words back into a string

# Example Usage
sentence = "Hello World from Codingal"
reverser = StringReverser(sentence)
print(reverser.reverse_words())  # Output: "Copilot from World Hello"

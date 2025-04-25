# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists",list(result))


#using map
nums = [1, 2, 3, 4, 5]  
square = list(map(lambda n: n * n, nums))
print(square)

words = ["hello", "world", "python"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(uppercase_words)

words = ["apple", "banana", "cherry"]
lengths = list(map(lambda word: len(word), words))
print(lengths)

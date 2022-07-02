text = "I study in UIU"

dictionary = {}

for i in range(len(text)):
    char = text[i]
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] = dictionary[char]+1
   
for char in dictionary:
    print(char,':',dictionary[char])
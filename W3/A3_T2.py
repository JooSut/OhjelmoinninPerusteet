print("Program starting.")
print("String comparisons")
word1 = input("Insert first word: ")
char = input("Insert character: ")
if(char in word1):
    print(f"Word \"{word1}\" contains character \"{char}\"")
else:
    print(f"Word \"{word1}\" doesn't contain character \"{char}\"")
    
word2 = input("Insert second word: ")
if(word1 < word2):
        print(f"The first word \"{word1}\" is before the second word \"{word2}\" alphabetically.")
elif(word2 < word1):
        print(f"The second word \"{word2}\" is before the first word \"{word1}\" alphabetically.")
else:
        print:("Both inserted words are the same alphabetically, \"{word1}\"")
        
print("Program ending.")
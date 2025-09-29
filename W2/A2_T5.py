#Start:
print("Program starting.\n")
#input:
word = input("Insert a closed compound word: ")
#in reverse:
backwards = word[::-1]
print(f"The word you entered is '{word}' and in reverse it is '{backwards}")
#Length:
length = len(word)
print(f"The inserted word length is {length}")
#Last character:
lc = word[-1]
print(f"Last character is '{lc}'\n")

#subtstring:
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
substring = word[start:end:step]

print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
#End program:
print("Program ending.")
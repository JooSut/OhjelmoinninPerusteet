print("Program starting.")
print("Testing decision structures.")

feed = input("Insert an integer: ")
value = int(feed)

print("Options:")
print("1 = In one multi-branched decisions")
print("2 = In multiple independent if statements")
print("0 = Exit")

feed = input("Your choice: ")
choice = int(feed)

if(choice == 1):
    print("Using one multi-branched decision structure.")
    if(value >= 400):
        #value = Value + 44
        value += 44
    elif(value >= 200):
        value += 22
    elif(value >= 100):
       value += 11
    print(f"Result is {value}")
elif(choice == 2):
    if(value >= 400):
        value += 44
    if(value >= 200):
        value += 22
    if(value >= 100):
       value += 11
    print(f"Result is {value}")
elif(choice == 0):
    print("Exiting...")
else:
    print("Unkown option")

print("\nProgram ending.")
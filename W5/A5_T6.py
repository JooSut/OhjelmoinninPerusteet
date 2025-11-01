def showOptions():
    print("Options:")
    print("1. Show count")
    print("2. Increase count")
    print("3. Reset count")
    print("0. Exit")


def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!\n")
        return -1


def main():
    print("Program starting.")
    counter = 0
    running = True

    while running:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count: {counter}\n")

        elif choice == 2:
            counter += 1
            print("Count increased!\n")

        elif choice == 3:
            counter = 0
            print("Cleared count!\n")

        elif choice == 0:
            print("Exiting program.")
            running = False

        elif choice != -1:
            print("Unknown option!\n")

    print("\nProgram ending.")

main()
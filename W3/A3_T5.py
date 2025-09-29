print("Program starting.\n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choise = int(input("Your choise: "))

if choise == 1:
    Celsius=float(input("Insert the amount of Celsius: "))
    Fahrenheit = Celsius * 1.8 + 32
    print(f"{round(Celsius, 1)} °C equals to {round(Fahrenheit, 1)} °F")
    print("\nProgram ending.")

elif choise == 2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit -32) /1.8
    print(f"{round(Fahrenheit, 1)} °F equals to {round(Celsius, 1)} °C")
    print("\nProgram ending.")

elif choise == 0:
    print("Exiting...")
    print("\nProgram ending.")
else:
    print("Unknown option.")
    print("\nProgram ending.")
print("Program starting.\n")
print("Check multiplicative persistence.")

# Ask for input
n = int(input("Insert an integer: "))

steps = 0

# Loop until single-digit or zero
while n >= 10 and n != 0:
    digits = [int(d) for d in str(n)]
    product = 1
    expression = " * ".join(str(d) for d in digits)

    # Compute product of digits
    for d in digits:
        product *= d

    # Print current step
    print(f"{expression} = {product}")

    # Prepare for next iteration
    n = product
    steps += 1

    # If result is 0, stop immediately
    if n == 0:
        print("No more steps.\n")
        break

# Print "No more steps" if loop ended normally
if n < 10:
    print("No more steps.\n")

print(f"This program took {steps} step(s)\n")
print("Program ending.")
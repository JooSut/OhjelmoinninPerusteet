print("Program starting.\n")
print("Check multiplicative persistence.")

n = int(input("Insert an integer: "))

steps = 0

while n >= 10 and n != 0:
    digits = [int(d) for d in str(n)]
    product = 1
    expression = " * ".join(str(d) for d in digits)

    for d in digits:
        product *= d

    print(f"{expression} = {product}")

    n = product
    steps += 1

    if n == 0:
        print("No more steps.\n")
        break

if n < 10:
    print("No more steps.\n")

print(f"This program took {steps} step(s)\n")
print("Program ending.")
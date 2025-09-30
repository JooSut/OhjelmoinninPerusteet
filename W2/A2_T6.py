print("Program starting.\n")

hex_color = input("Insert a hex color: ")

if len(hex_color) == 7 and hex_color[0] == '#' and all(c in "0123456789abcdefABCDEF" for c in hex_color[1:]):
    red_hex = hex_color[1:3]
    green_hex = hex_color[3:5]
    blue_hex = hex_color[5:7]

    # Convert hex strings to integers
    red = int(red_hex, 16)
    green = int(green_hex, 16)
    blue = int(blue_hex, 16)

    print("\nColors")
    print(f"-Red {red_hex}")
    print(f"-Green {green_hex}")
    print(f"-Blue {blue_hex}")

    print("\nProgram ending.")
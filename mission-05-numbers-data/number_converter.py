def main():
    user_input = input("Enter a decimal number: ")
    number = int(user_input)
    
    binary_str = bin(number)
    hex_str = hex(number)
    
    print(f"Decimal: {number}")
    print(f"Binary: {binary_str}")
    print(f"Hexadecimal: {hex_str}")

if __name__ == "__main__":
    main()

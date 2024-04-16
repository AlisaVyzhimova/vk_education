def main():

    input_string = input("Введите строку: ")

    input_string = input_string.lower()

    replaced_symbols = "!%#@"
    for symbol in replaced_symbols:
        input_string = input_string.replace(symbol, '')
        
    count_replaced = len(replaced_symbols) - len(input_string)
    print(count_replaced)
    print(input_string)

if __name__ == "__main__":
    main()

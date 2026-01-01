menu = input(' A. Addition\n B. Subtraction\nenter the number: ').lower()

if menu == 'a':
    addition_list = list()
    while True:
        number = input('Add a number (C to cancel): ')
        try:
            number = int(number)
            addition_list.append(number)
        except:
            if number.lower()[0] == 'c':
                break
        print(f'Result: {sum(addition_list)}')

elif menu == 'b':
    subtraction_list = list()
    while True:
        number2 = input('Add a number (C to cancel): ')
        try:
            number2 = int(number2)
            subtraction_list.append(number2)
        except:
            if number2.lower()[0] == 'c':
                break

        result = subtraction_list[0]
        for n in subtraction_list[1:]:
            result -= n
        print(f'Result: {result}')

    
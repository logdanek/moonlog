def greatest_common_divisor(arg_1, arg_2):
    """
    Функция нахождения НОД 2 неотрицательных чисел
    """
    numbers = [arg_1, arg_2]
    remainder = 10
    if numbers[0] == 0:  # Частные случаи
        return numbers[1]
    if numbers[1] == 0:
        return numbers[0]

    while remainder != 0:
        remainder = max(numbers[0], numbers[1]) - min(numbers[0], numbers[1]) \
                    * (max(numbers[0], numbers[1]) // min(numbers[0], numbers[1]))
        if numbers[0] < numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        numbers[0], numbers[1] = numbers[1], remainder
    return 'gcd(' + str(arg_1) + ',' + str(arg_2) + ')' + ' ' + '=' \
            + ' ' + str(numbers[0])


first_number, second_number = map(int, input('Введите 2 неотрицательных числа' \
                              + '\n' + 'Ex. 12 24 \n').split())  # Ввод чисел

print(greatest_common_divisor(first_number, second_number))

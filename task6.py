def linear_gcd(arg_1, arg_2):
    """
    Функция, выдающее линейное представление НОД двух чисел
    """
    if arg_1 == 0:
        return (arg_2, 0, 1)
    divisor, x_multiplier, y_multiplier = linear_gcd(arg_2 % arg_1, arg_1)
    return (divisor, y_multiplier - (arg_2 // arg_1) * x_multiplier, x_multiplier)


first_number, second_number = map(int, input('Введите 2 неотрицательных числа' \
                              + '\n' + 'Ex. 12 24 \n').split())  # Ввод чисел
result_list = linear_gcd(first_number, second_number)
if result_list[1] > 0 and result_list[2] > 0:
    print('gcd' + '(' + str(first_number) + ',' + str(second_number) + ')' + ' = ' +
          str(result_list[0]) + ' = ' + str(first_number) + '*' + str(result_list[1])
          + ' + ' + str(second_number) + '*' + str(result_list[2]))
elif result_list[1] > 0 and result_list[2] < 0:
    print('gcd' + '(' + str(first_number) + ',' + str(second_number) + ')' + ' = ' +
          str(result_list[0]) + ' = ' + str(first_number) + '*' + str(result_list[1])
          + ' + ' + str(second_number) + '*' + '(' + str(result_list[2]) + ')')
else:
    print('gcd' + '(' + str(first_number) + ',' + str(second_number) + ')' + ' = ' +
          str(result_list[0]) + ' = ' + str(first_number) + '*' + '(' + str(result_list[1])
          + ')' + ' + ' + str(second_number) + '*' + str(result_list[2]))

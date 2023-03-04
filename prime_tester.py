import random
import sys


def two_factorization(some_number):
    """
    Раскладывание числа n в виде: some_number = (2 ** number_of_twoes) * multiplier
    """
    multiplier = 0
    number_of_twoes = 0
    temp_variable = some_number - 1
    while temp_variable % 2 == 0:
        number_of_twoes += 1
        temp_variable //= 2
    multiplier = (some_number - 1) // (2 ** number_of_twoes)
    result = [number_of_twoes, multiplier]
    return result


def is_prime(potential_prime, ITERATIONS = 6):
    """
    Проверка числа на простоту с помощью теста Миллера - Рабина
    potential_prime -- принимаемое на вход число
    ITERATIONS -- параметр точности проверки -- число перебираемых возможных
                  свидетелей простоты числа potential_prime по Миллеру
    """
    if potential_prime == 1:
        return False, 1
    if potential_prime == 2 or potential_prime == 3:
        return True, 1
    if potential_prime % 2 == 0:
        return False, 1
    number_of_twoes, multiplier = two_factorization(potential_prime)[0], \
                                  two_factorization(potential_prime)[1]
    for i in range(ITERATIONS):
        evidence_number = random.randint(2, potential_prime - 2)
        cheking_number = (evidence_number ** multiplier)
        temp_variable = cheking_number % potential_prime
        if temp_variable != 1:
            for r in range(0, number_of_twoes):
                second_temp_variable = (cheking_number ** (2 ** r)) % potential_prime
                if second_temp_variable == potential_prime - 1:
                    break
                if r == number_of_twoes - 1:
                    return False, 1
        return True, 4 ** (- ITERATIONS)
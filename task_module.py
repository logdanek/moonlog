import random
import matplotlib.pyplot as mpl
import prime_tester


def count_primes(amount: int):
    """
    Ответ на вопрос: Сколько простых чисел в amount случайных?
    """
    count = 0
    numbers = []
    for i in range(amount):
        numbers.append(random.randint(1, 1000))
    for i in numbers:
        if prime_tester.is_prime(i)[1]:
            count += 1
    return count


def graph_primes(amount: int, tests: int):
    """
    Построение гистограммы: сколько простых чисел count среди amount
    случайных в результате tests тестов
    """
    count = [count_primes(amount) for i in range(tests)]
    print("---")
    print(count)
    mpl.hist(count)
    mpl.show()


A, B = map(int, input('Введите количество чисел и количество испытаний \
    \n Ex. 200 8 \n').split())
graph_primes(A, B)

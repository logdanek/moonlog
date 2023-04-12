import time
import multiprocessing
import prime_tester

def test_all(pool):
    l = pool.map(prime_tester.is_prime, range(1_000_000, 1_000_100))
    return l


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print("__name__:", __name__)
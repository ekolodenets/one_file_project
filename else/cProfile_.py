import cProfile
import pstats
import time

def add(x, y):
    result = 0
    result += x
    result += y
    return result


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def do_stuff():
    result = []
    for i in range(10000000):
        result.append(i**2)
    return result


def waste_time():
    time.sleep(5)
    print('Time is wasted')


if __name__ == '__main__':
    with cProfile.Profile() as profile:
        print(add(100, 500))
        print(fact(1000))
        print(do_stuff())
        waste_time()

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
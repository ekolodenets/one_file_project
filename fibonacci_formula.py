import timeit
def fibona(n):
    b = (1 + 5**0.5)**n / (2**n * 5**0.5)
    return round(b)

start_time = timeit.default_timer()
print(fibona(600))
print(timeit.default_timer() - start_time)
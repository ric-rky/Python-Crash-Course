fib_dict = {0: 0, 1: 1}

def fib(n):
    if n in fib_dict:
        return fib_dict[n]
    fib_dict[n] = fib(n - 1) + fib(n - 2)
    return fib_dict[n]

even_fib_sum = 0
n = 0

while True:
    fib_n = fib(n)
    if fib_n > 4 * 10 ** 6:
        break
    if fib_n % 2 == 0:
        even_fib_sum += fib_n
    n += 1

print(even_fib_sum)










def linear_congruential_generator(count, seed, a=1664525, c=1013904223, m=2**32):
    x = seed
    numbers = []
    for _ in range(count):
        x = (a * x + c) % m
        numbers.append(x)
    return numbers


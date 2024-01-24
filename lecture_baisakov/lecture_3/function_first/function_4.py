def only_prime_numbers(numbers: str) -> list:
    return [i for i in list(map(int, numbers.split())) if len([j for j in range(2, i) if i % j == 0]) == 0 and i > 1]

print(only_prime_numbers('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23'))

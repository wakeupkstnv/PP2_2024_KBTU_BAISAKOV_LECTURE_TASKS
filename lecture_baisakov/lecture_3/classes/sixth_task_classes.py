x = lambda n: [_ for _ in n if not len([True for i in range(2, _) if _ % i == 0 ]) and _ != 1]
print(x(list(range(1, 20))))

from itertools import permutations

def permutation(word: str) -> str:
    return (''.join(_) for _ in permutations(word))

print(list(permutation('')))
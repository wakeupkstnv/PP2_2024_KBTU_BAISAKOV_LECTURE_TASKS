def IsPalindrome(word: str) -> bool:
    return True if word[::-1] == word else False

print(IsPalindrome('madam'))
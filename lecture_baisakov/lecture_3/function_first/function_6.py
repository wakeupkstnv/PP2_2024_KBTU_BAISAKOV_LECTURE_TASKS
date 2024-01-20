reverse_words = lambda word: [_ for _ in list(word.split())[::-1]]
print(' '.join(reverse_words('we are using the python')))
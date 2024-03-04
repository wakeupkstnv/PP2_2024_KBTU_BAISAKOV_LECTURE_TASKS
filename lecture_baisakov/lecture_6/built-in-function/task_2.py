word = 'BrawlStars'
lower_letter, upper_letter = [], []

x = [lower_letter.append(1) if _.islower() else upper_letter.append(1) if _.isupper() else None for _ in word]
print(f'lower: {len(lower_letter)}, upper: {len(upper_letter)}')
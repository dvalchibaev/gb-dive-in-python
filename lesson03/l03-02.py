"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""
from collections import Counter

with open('anti-gravity.txt') as f:
    input_text = ''.join([letter for letter in f.read() if letter.isalpha() or letter.isspace()]).split()

text_stats = Counter(input_text)
most_common = [word[0] for word in text_stats.most_common(10)]
print(f'Наиболее часто встречающиеся слова {most_common}')

"""
Задача 2

Създайте функция, която да връща броя на гласните в даден текст (нека за улеснение считаме за гласни само `a`, `e`, `i`, `o`, `u`).
"""


def number_of_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sum = 0

    for char in text:
        if char.lower() in vowels:
            sum += 1

    return sum


print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)

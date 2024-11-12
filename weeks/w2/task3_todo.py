"""
Задача 3

Създайте функция, която проверява дали дадено българско ЕГН е [валидно](https://bg.wikipedia.org/wiki/Единен_граждански_номер#Структура).

По-конкретно, функцията трябва:
* да има за първи задължителен параметър ЕГН-то (очаква се да е `str`, но може да се опитате и да го направите да работи едновременно и за `str`, и за `int`).
* да има именован параметър `bypass_checksum`, който по подразбиране е `False`. Ако е `True`, функцията трябва да НЕ проверява валидността на последната цифра, а да я счита за валидна по подразбиране.
* да връща `True` ако ЕГН-то е валидно, `False` в противен случай. За валидно ЕГН се смята такова, при което:
    * цифрите за месец и ден съответстват на валидна дата. Това означава цифрите на месеца да са в интервала [1, 12] за хора, родени 1900-2000г. и в интервала [41, 52] за хора, родени след 2000г., като пожелание може да проверявате и за интервала [21, 32] за хора, родени преди 1900г.
    * Ако `bypass_checksum` e `False`, то последната 1 цифра трябва да е валиден checksum на останалите. Алгоритъмът за изчисляване на последната цифра може да намерите [тук](https://bg.wikipedia.org/wiki/Единен_граждански_номер#Структура).
"""


def is_valid_ucn(ucn, *, bypass_checksum=False):
    pass  # write your code here

print(is_valid_ucn("6101057509") == True)
print(is_valid_ucn("6101057500", bypass_checksum=True) == True)
print(is_valid_ucn("6101057500") == False)
print(is_valid_ucn("6913136669") == False)
"""
Задача 1

Създайте функция, която приема число, указващо брой секунди и го връща трансформирано в наредена тройка от часове, минути и секунди.
Например
3661 -> (1, 1, 1), понеже 3661 секунди са 1hr 1min 1sec.
86399 -> (23, 59, 59), понеже 86399 секунди са 23hr 59min 59sec. и т.н.
"""


def seconds_to_time(seconds):
    hour = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    return hour, minutes, seconds


print(seconds_to_time(0) == (0, 0, 0))
print(seconds_to_time(1) == (0, 0, 1))
print(seconds_to_time(69) == (0, 1, 9))
print(seconds_to_time(420) == (0, 7, 0))
print(seconds_to_time(3661) == (1, 1, 1))
print(seconds_to_time(86399) == (23, 59, 59))
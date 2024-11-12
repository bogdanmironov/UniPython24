# Write your code here
def take(iterable, n):
    return (item for i, item in filter(lambda x: x[0] < n if n >= 0 else x[0] >= len(iterable) + n, enumerate(iterable)))

sample = [1, 2, 3, 4, 5, 6]

expected_1 = [1, 2, 3]
actual_1 = list(take(sample, 3))

expected_2 = []
actual_2 = list(take(sample, 0))

expected_3 = [1, 2, 3, 4, 5, 6]
actual_3 = list(take(sample, 10))

expected_4 = [1, 2, 3, 4]
actual_4 = list(take(sample, 4))

expected_5 = [5, 6]
actual_5 = list(take(sample, -2))

expected_6 = [3, 4, 5, 6]
actual_6 = list(take(sample, -4))

assert expected_1 == actual_1
assert expected_2 == actual_2
assert expected_3 == actual_3
assert expected_4 == actual_4
assert expected_5 == actual_5
assert expected_6 == actual_6

print("✅ All OK! +0.75 points")
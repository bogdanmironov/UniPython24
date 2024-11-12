def sdrawkcab(function):
    def inner(*args):
        res = function(*args)
        match res:
            case str():
                return res[::-1]
            case list():
                return [item[::-1] if isinstance(item, str) else item for item in res]
            case _:
                return res
    return inner

@sdrawkcab
def my_string_function(name):
    return f"Hello, {name}"

@sdrawkcab
def my_non_string_function():
    return 42

@sdrawkcab
def list_of_strings():
    return ["ab", "yaj", "yaj"]

@sdrawkcab
def list_of_ints():
    return [15, 16]

@sdrawkcab
def mixed_list():
    return [15, 16, "si", "a", "doog", "ecalp", "ot", "evah", "a", "reeb", "."]

expected_my_string_function_1 = "obuyL ,olleH"
expected_my_non_string_function = 42
expected_my_string_function_2 = "backwards ,olleH"
expected_list_of_strings = ["ba", "jay", "jay"]
expected_list_of_ints = [15, 16]
expected_mixed_list = [15, 16, "is", "a", "good", "place", "to", "have", "a", "beer", "."]

assert my_string_function("Lyubo") == expected_my_string_function_1
assert my_non_string_function() == expected_my_non_string_function
assert my_string_function("sdrawkcab") == expected_my_string_function_2
assert list_of_strings() == expected_list_of_strings
assert list_of_ints() == expected_list_of_ints
assert mixed_list() == expected_mixed_list

print("✅ All OK! +1 points")
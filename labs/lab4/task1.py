import os


def validate_list(path: str) -> int:
    try:
        with open(path) as fd:
            lines = fd.readlines()

            print(lines)

            sum = 0
            for line in lines:
                if line[0] != '-':
                    raise InvalidLineError(line)
                line = line[1:]
                line = line[:-2]

                if line[0] == ' ':
                    line = line[1:]

                tokens = line.split(':')


                if not (tokens[0].isalnum() and tokens[1].isnumeric() and tokens[2].isnumeric()):
                    raise InvalidLineError(line)


            return sum
    except FileNotFoundError as e:
        raise ListFileError(path)


class InvalidLineError(Exception):
    def __init__(self, line: str) -> None:
        super().__init__(f'There was invalid line: {line}')


class InvalidItemError(Exception):
    def __init__(self, item_name: str) -> None:
        super().__init__(f'Invalid item: {item_name}')


class InvalidQuantityError(Exception):
    def __init__(self, quantity: int, item_name: str) -> None:
        super().__init__(f'Invalid quantity of {item_name}: {quantity}')


class InvalidPriceError(Exception):
    def __init__(self, price: int, item_name: str) -> None:
        super().__init__(f'Invalid price of {item_name}: {price}')


class ListFileError(Exception):
    def __init__(self, path: str = '') -> None:
        super().__init__(f'File is not found. Path: \n {path}')


# assert abs(validate_list(os.path.join("lab04_files", "task_1", "list1.txt")) - 11.25) < 0.001
#
# assert int(validate_list(os.path.join("lab04_files", "task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("lab04_files", "task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError - 3"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError - 4"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list5.txt"))
    assert False, "Should raise InvalidItemError - 5"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list6.txt"))
    assert False, "Should raise InvalidQuantityError - 6"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list7.txt"))
    assert False, "Should raise InvalidQuantityError - 7"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list8.txt"))
    assert False, "Should raise InvalidQuantityError - 8"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list9.txt"))
    assert False, "Should raise InvalidPriceError - 9"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list10.txt"))
    assert False, "Should raise InvalidPriceError - 10"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError - 11"
except InvalidLineError:
    pass

print("✅ All OK! +2 points")

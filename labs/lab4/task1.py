import os


def validate_list(path: str) -> int:
    try:
        with open(path) as fd:
            total_price = 0
            for line in fd:
                if line[0] != '-':
                    raise InvalidLineError(line)

                line = line.strip()[1:]

                if line[0] == ' ':
                    line = line[1:]

                try:
                    item_name, item_count, item_price = line.split(':')
                except ValueError:
                    raise InvalidLineError(line)

                if not item_name or item_name.isdigit():
                    raise InvalidItemError(item_name)

                if not item_count.isdigit():
                    raise InvalidQuantityError(item_price, item_name)
                item_count = int(item_count)

                try:
                    item_price = float(item_price)

                    if item_price < 0:
                        raise InvalidPriceError(item_price, item_name)
                except ValueError:
                    raise InvalidPriceError(item_price, item_name)

                total_price += item_count * item_price

            return total_price
    except (FileNotFoundError, PermissionError):
        raise ListFileError(path)
    # except PermissionError:
    #     raise ListFileError(path)


class InvalidLineError(Exception):
    def __init__(self, line: str) -> None:
        super().__init__(f'There was invalid line: {line}')


class InvalidItemError(Exception):
    def __init__(self, item_name: str) -> None:
        super().__init__(f'Invalid item: {item_name}')


class InvalidQuantityError(Exception):
    def __init__(self, quantity: str, item_name: str) -> None:
        super().__init__(f'Invalid quantity of {item_name}: {quantity}')


class InvalidPriceError(Exception):
    def __init__(self, price: float | int, item_name: str) -> None:
        super().__init__(f'Invalid price of {item_name}: {price}')


class ListFileError(Exception):
    def __init__(self, path: str = '') -> None:
        super().__init__(f'File is not found. Path: \n {path}')


assert abs(validate_list(os.path.join("task_1", "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join("task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("task_1", "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("task_1", "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("task_1", "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

print("✅ All OK! +1 point")
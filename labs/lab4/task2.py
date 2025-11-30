from collections import deque
# Preconditions
import os


class LAIKA:
    def __init__(self, path: str, caesar_key: int) -> None:
        self.path = path
        self.caesar_key = caesar_key

    @staticmethod
    def encode(string: str, n: int) -> list[str]:
        at_start = True
        le, r = "", ""

        for char in string:
            if at_start:
                le = le + char
                at_start = False
            else:
                r = char + r
                at_start = True

        result = le + r
        return [result[i:i+n] for i in range(0, len(result), n)]

    @staticmethod
    def decode(encoded: list[str]) -> str:
        encoded = "".join(encoded)
        at_start = True
        result = ""

        for _ in encoded:
            if at_start:
                result += encoded[0]
                encoded = encoded[1:]
                at_start = False
            else:
                result += encoded[-1]
                encoded = encoded[:-1]
                at_start = True

        return result

    def encrypt(self, text: str) -> str:
        result = ""

        for char in text:
            if char.isupper():
                result += chr((ord(char) + self.caesar_key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + self.caesar_key - 97) % 26 + 97)

        return result

    def encode_to_files(self, text: str, n: int) -> str:
        list_of_encoded_strings = self.encode(text, n)
        first_file_name = self.encrypt(list_of_encoded_strings[0])

        for i in range(len(list_of_encoded_strings)):
            encrypted_string = self.encrypt(list_of_encoded_strings[i])

            with open(os.path.join(self.path, encrypted_string), 'x') as fd:
                if i < len(list_of_encoded_strings) - 1:
                    next_encrypted_string = self.encrypt(list_of_encoded_strings[i + 1])
                    fd.write(next_encrypted_string + '\n')
                else:
                    fd.write('\n')

                fd.write(list_of_encoded_strings[i])

        return first_file_name

    def decode_from_files(self, file_name: str) -> str:
        res = []

        while file_name:
            with open(os.path.join(self.path, file_name)) as fd:
                first_line = fd.readline().strip()
                second_line = fd.readline()

                if first_line:
                    res += [second_line]
                else:
                    res += [second_line]

                file_name = first_line

        return self.decode(res)


root_dir = "task_2"
os.makedirs(root_dir)

l = LAIKA(root_dir, 3)

# encode
assert l.encode("abcdefg", 2) == ["ac", "eg", "fd", "b"]
assert l.encode("abcdefg", 3) == ["ace", "gfd", "b"]
assert l.encode("abcdefg", 5) == ["acegf", "db"]
assert l.encode("abcdefghijkl", 1) == ["a", "c", "e", "g", "i", "k", "l", "j", "h", "f", "d", "b"]
assert l.encode("abcdefghijkl", 2) == ["ac", "eg", "ik", "lj", "hf", "db"]
assert l.encode("abcdefghijkl", 3) == ["ace", "gik", "ljh", "fdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 12) == ["acegikljhfdb"]
assert l.encode("abcdefghijkl", 24) == ["acegikljhfdb"]


# decode
assert l.decode(["ac", "eg", "fd", "b"]) == "abcdefg"
assert l.decode(l.encode("abcdefg", 3)) == "abcdefg"
assert l.decode(l.encode("abcdefg", 5)) == "abcdefg"
assert l.decode(l.encode("abcdefghijkl", 1)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 2)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 3)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 12)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 24)) == "abcdefghijkl"


# encode_to_files
l1 = LAIKA(root_dir, 4)
assert l1.encode_to_files("abcdefghijkl", 3) == "egi"

assert sorted(os.listdir(root_dir)) == ["egi", "jhf", "kmo", "pnl"]

with open(os.path.join(root_dir, "egi")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "kmo"
assert content == "ace"

with open(os.path.join(root_dir, "jhf")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == ""
assert content == "fdb"

with open(os.path.join(root_dir, "kmo")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "pnl"
assert content == "gik"

with open(os.path.join(root_dir, "pnl")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "jhf"
assert content == "ljh"


# decode_from_files
assert l1.decode_from_files("egi") == "abcdefghijkl"

# Exception

try:
    l1.encode_to_files("abcdefghijkl", 3)
except FileExistsError:
    assert True
except Exception:
    assert False


try:
    l1.decode_from_files("non-existing-file")
except FileNotFoundError:
    assert True
except Exception:
    assert False

print("✅ All OK! +2 points")

'''
Задача 5 (0.75т.)
Напишете клас Person, който да репрезентира човек:

Да притежава член-данни:

name: низ (str) - име на човека от семейството

age: цяло число (int) - възраст на човека

Да реализира следните методи:

__repr__: Метода трябва да връща низ (str) с подходяща Python репрезентация на обекта

__str__: Метода трябва да връща низ (str), представляващ име на човека и неговите години във формат Name (age)

__gt__: Предефинирайте оператора > (greater than), който да сравнява два човека (Person) спрямо годините им.

Напишете клас FamilyTree, който да репрезентира родословно дърво:

Да притежава член-данни:

root: обект от тип Person представляващ главата на едно родословно дърво

children: list от елементи от същия клас (Family_Tree) - Наследници на човека от семейство. Всяко дете си е корен на своето родословно дърво. По подразбиране един човек няма деца. (hint be carefull with default empty lists)

Да реализира следните методи:

__str__: Метода трябва да връща низ (str), представляващ построеното родословно дърво с корен root. За всеки Person в дървото трябва да са изведени неговото име и години във формат > Name (age), като пред всеки реди поставяме 4 4 празни места, спрямо нивото му в дървото. Ако човекът има деца, подреждаме информацията за тях спрямо реда им на добавяне. (hint поздрави от дискретна математика) .

Пример:
> John (50)
    > Jake (18)
    > Emily (30)
        > Dan (3)
        > Fiona (7)
count_descendants: Рекурсивен метод който да връща броя на наследници на корена да дървото (int) (деца, внуци, правнуци, праправнуци, ...). Например "Boyko has 69 descendants"

add_child_tree: Метод който да добавя дете (друг Family_Tree обект) към списъка с деца.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'

    __repr__ = __str__

    def __gt__(self, other):
        return self.age > other.age


class FamilyTree:
    def __init__(self, root, children=None):
        if children is None:
            children = []
        self.root = root
        self.children = children

    def __str__(self, num_of_parents=0):
        res = f'> {self.root}\n'

        for child in self.children:
            for _ in range(num_of_parents+1):
                res += '    '
            res += f'{child.__str__(num_of_parents+1)}'

        return res

    def count_descendants(self):
        res = 0

        for child in self.children:
            res += 1 + child.count_descendants()

        return res

    def add_child_tree(self, child_tree):
        self.children.append(child_tree)


# tests

# Create dummies of class Person
john = Person("John", 50)
emily = Person("Emily", 30)
jake = Person("Jake", 18)
dan = Person("Dan", 3)
fiona = Person("Fiona", 7)

# Create family trees for each person
john_familiy_tree = FamilyTree(john)
emily_familiy_tree = FamilyTree(emily)
jake_familiy_tree = FamilyTree(jake)
dan_familiy_tree = FamilyTree(dan)
fiona_familiy_tree = FamilyTree(fiona)

# ---- Testing add_child_tree functionality ----

# Add children to John
john_familiy_tree.add_child_tree(jake_familiy_tree)
john_familiy_tree.add_child_tree(emily_familiy_tree)

# Add children to Emily
emily_familiy_tree.add_child_tree(dan_familiy_tree)
emily_familiy_tree.add_child_tree(fiona_familiy_tree)

assert john_familiy_tree.children[1] == emily_familiy_tree
assert john_familiy_tree.children[0] == jake_familiy_tree
assert emily_familiy_tree.children[0] == dan_familiy_tree
assert emily_familiy_tree.children[1] == fiona_familiy_tree

# ---- Testing __init__ functionality ----

assert john.name == "John"
assert john.age == 50

assert jake.name == "Jake"
assert jake.age == 18

assert john_familiy_tree.root == john
assert len(john_familiy_tree.children) == 2

assert jake_familiy_tree.root == jake
assert len(jake_familiy_tree.children) == 0

assert emily_familiy_tree.root == emily
assert dan_familiy_tree.root == dan
assert fiona_familiy_tree.root == fiona

# ---- Testing __str__functionality ----
expected_repr = "> John (50)\n    > Jake (18)\n    > Emily (30)\n        > Dan (3)\n        > Fiona (7)\n"
assert str(john_familiy_tree) == expected_repr

# # ---- Testing __gt__functionality ----
assert john > emily
assert john > jake
assert emily > jake
assert jake > dan

# # ---- Testing __gt__functionality ----
assert john_familiy_tree.count_descendants() == 4
assert jake_familiy_tree.count_descendants() == 0
assert emily_familiy_tree.count_descendants() == 2

print("✅ All OK! +0.75 points")

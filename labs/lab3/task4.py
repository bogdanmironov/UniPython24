import itertools
import collections

coordinates = [[0,0],[0,1],[0,-1]]
print(set([el[0] for el in coordinates]) == 1)
pairs = list(itertools.pairwise(coordinates))
differences = [(second[0] - first[0], second[1] - first[1]) for first, second in pairs]
print(differences)
print(len(set(differences)))
print(differences[0][1] - differences[0][0])


def checkStraightLine(coordinates):
    (x0, y0), (x1, y1) = coordinates[:2]
    dx, dy = x1 - x0, y1 - y0

    return all([False if dy * (x - x0) != dx * (y - y0) else True for x, y in coordinates[2:]])

    for x, y in coordinates[2:]:
        if dy * (x - x0) != dx * (y - y0):
            return False
    return True


print(checkStraightLine(coordinates))
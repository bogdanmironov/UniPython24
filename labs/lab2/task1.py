from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('Rectangle', ['start', 'end', 'area'])


def calculate_area(a, b):
    width = abs(a.x - b.x)
    height = abs(a.y - b.y)

    return width * height


def get_areas(starting_points, ending_points, n):
    list_rectangles = [Rectangle(start, end, calculate_area(start, end)) for start, end in zip(starting_points, ending_points)]
    filtered_rectangles = list(filter(lambda obj: obj.area > n, list_rectangles))
    sorted_filtered_rectangles = list(reversed(sorted(filtered_rectangles, key=lambda obj: obj.area)))
    return sorted_filtered_rectangles


starting_points = [
    Point(2, 3),
    Point(0, 0),
    Point(3, 4),
    Point(5, 6),
    Point(3, 3),
]
ending_points = [
    Point(3, 4),
    Point(-5, -9),
    Point(7, 7),
    Point(5, 6),
    Point(0, 0),
]

expected_result = [
    Rectangle(Point(x=0, y=0), Point(x=-5, y=-9), 45),
    Rectangle(Point(x=3, y=4), Point(x=7, y=7), 12),
]

assert get_areas(starting_points, ending_points, 9) == expected_result

starting_points_2 = [
    Point(3, 4),
    Point(2, 3),
    Point(5, 6),
    Point(3, 3),
    Point(0, 0),
]
ending_points_2 = [
    Point(7, 7),
    Point(3, 4),
    Point(5, 6),
    Point(0, 0),
    Point(-5, -9),
]

expected_result_2 = [
    Rectangle(Point(x=0, y=0), Point(x=-5, y=-9), 45),
    Rectangle(Point(x=3, y=4), Point(x=7, y=7), 12),
]

assert get_areas(starting_points_2, ending_points_2, 9) == expected_result_2

print("✅ All OK! +0.75 point")
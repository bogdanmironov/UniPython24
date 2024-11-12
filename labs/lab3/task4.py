#Leetcode problem 1232. Check If It Is a Straight Line
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        dx, dy = x1 - x0, y1 - y0

        return all([False if dy * (x - x0) != dx * (y - y0) else True for x, y in coordinates[2:]])

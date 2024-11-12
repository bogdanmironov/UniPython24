#Leetcode problem 1337. The K Weakest Rows in a Matrix
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        enumerated = list(enumerate(mat))
        enumerated.sort(key=lambda x: x[1])
        return [element[0] for element in enumerated[:k]]

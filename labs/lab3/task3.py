'''
Task: Leetcode - 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.
'''
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(Solution().majorityElement(nums1))
print(Solution().majorityElement(nums2))

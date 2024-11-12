#Leetcode problem 500. Keyboard Row
from typing import List

first = set("qwertyuiop")
second = set("asdfghjkl")
third = set("zxcvbnm")


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [word 
                for word in words 
                if (set_word := set(word.lower())) <= first 
                or set_word <= second 
                or set_word <= third]

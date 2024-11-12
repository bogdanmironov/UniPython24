import string

first = set("qwertyuiop")
second = set("asdfghjkl")
third = set("zxcvbnm")

class Solution():
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word \
                for word in words \
                if (set_word := set(word.lower())) <= first \
                or set_word <= second \
                or set_word <= third]

        # return [word for word in words if (set_word := set(word.lower())) <= first or set_word <= second or set_word <= third]
        # return [word for word in words if set(word) <= first or set(word) <= second or set(word) <= third]

words = ["Hello", "Alaska", "Dad", "Peace"]
print([set_word for word in words if (set_word := set(word.lower()))])
sol = Solution()
print(sol.findWords(words))
print(first)
# Notes from this problem:
# nonlocal keyword used when you want to modify a variable outside of the current scope of a function

# clever trick to make solution O(n) time complexity -
# - is to check if n-1 exists, therefore you know that n is not the start of a sequence, saving you from counting every number

class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0

        def countFromX(x):
            nonlocal longest
            counter = 0
            currNum = x
            while currNum in numSet:
                counter += 1
                currNum += 1

            if longest < counter:
                longest = counter

        for num in numSet:
            if (num - 1) in numSet:
                continue
            else:
                countFromX(num)

        return longest

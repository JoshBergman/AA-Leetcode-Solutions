# Originally solved as an optimized brute force solution (bottom of file)
# Partly because I didnt take into account that the list was already sorted

# solution 2
# takes advantage of the fact that the list is sorted

# solution 2 - closing window
def twoSum(self, numbers, target: int):
    left = 0
    right = len(numbers) - 1

    while True:
        currSum = numbers[left] + numbers[right]
        if currSum == target:
            return [left + 1, right + 1]

        # when sum is too large, decrease larger number (right)
        if currSum > target:
            right -= 1
            continue

        # when sum is too small increase lower number (left)
        if currSum < target:
            left += 1
            continue


# solution 1 - optimized brute force
def twoSumFirstAttempt(self, numbers, target: int):
    pointer = 1
    laggingPointer = 0

    while laggingPointer < len(numbers):
        lagNum = numbers[laggingPointer]
        while pointer < len(numbers) and numbers[pointer] <= (target - lagNum):
            sum = numbers[pointer] + lagNum
            if sum == target:
                return [laggingPointer + 1, pointer + 1]
            pointer += 1

        # update lagging pointer while skipping dupes
        while lagNum == numbers[laggingPointer] or numbers[laggingPointer] > target:
            laggingPointer += 1

        pointer = laggingPointer + 1
    return [1, 2]

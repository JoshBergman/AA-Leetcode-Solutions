#With this problem I had to get clever with how I thought about it
# Instead of trying to think of how to maximize an array,
# I thought about how actual water would flow in a container,
# Which led me to this solution based on finding the containers walls

# worst case of O(N) beats 99.5% of python submissions

def maxArea(self, height: [int]) -> int:
        largestArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            leftVal = height[left]
            rightVal = height[right]
            
            shortest = rightVal if rightVal < leftVal else leftVal
            thisArea = (right - left) * shortest

            if thisArea > largestArea:
                largestArea = thisArea
            
            if leftVal < rightVal:
                left += 1
            else:
                right -= 1

        return largestArea
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we'll have converging pointers
        # one starts from beginning index other from the end
        # right pointer would be used to weed out elements we don't need
        # and left pointer to traverse through the elements

        # left pointer begins at 0
        left = 0

        # right pointer begins at end
        right = len(numbers) - 1
        # to store result
        result = []
        # to store current sum
        sum = 0

        while left < right:
            sum = numbers[left] + numbers[right]
            # if target smaller, weed out larger element by decrementing right pointer
            if sum > target:
                right -= 1
            # if target larger, progress left to next element by incrementing
            elif sum < target:
                left += 1
            # if target same, return result
            else:
                result = [left + 1, right + 1]
                return result
        return result


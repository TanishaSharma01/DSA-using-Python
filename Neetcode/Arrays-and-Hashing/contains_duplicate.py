# NEETCODE 150
# https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        
        for num in nums:
            if num in result:
                return True
            result.add(num)
        return False
    
sol = Solution()

print(sol.hasDuplicate([1,2,4,5,6]))
print(sol.hasDuplicate([1,2,4,5,5]))
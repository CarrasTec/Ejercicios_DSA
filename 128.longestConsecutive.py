class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        ans = 0

        for i in nums:
            if not ((i-1) in mySet):
                count = 0
                while (i+count) in mySet:
                    count += 1
                ans = max(ans, count)
        
        return ans

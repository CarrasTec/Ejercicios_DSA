class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() #O(n Log n)

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            b = i+1
            c = len(nums) - 1

            while b < c:
                sum3 = a + nums[b] + nums[c]
                if sum3>0:
                    c -= 1
                elif sum3<0:
                    b += 1
                else:
                    ans.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while nums[b] == nums[b-1] and b<c:
                        b += 1
            
        return ans

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in nums[i+1:]:
                res.append(i)
                res.append(nums.index(comp,i+1))
                return res
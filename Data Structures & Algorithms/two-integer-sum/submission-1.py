class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i= 0
        out = []
        for i in range(len(nums)):
            for j in range(i+1,(len(nums))):
                if nums[i]+nums[j] == target:
                    out.append(i)
                    out.append(j)
                    return out 
                j+=1
            i+=1         
            
        
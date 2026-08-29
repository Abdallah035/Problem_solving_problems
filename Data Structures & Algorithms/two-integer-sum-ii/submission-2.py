class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        po1 = 0
        po2 = len(numbers)-1
        while (po1 < po2 ):
            if numbers[po1]+ numbers[po2] == target:
                return [po1+1,po2+1]
            elif numbers[po1]+ numbers[po2] > target:
                po2 -=1
            else:
                po1+=1    


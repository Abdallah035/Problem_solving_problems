class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_res={}
        res = []
        for num in nums:
            if num not in dict_res:
               dict_res[num] = 0
            dict_res[num] += 1
        sorted_keys = sorted(dict_res, key=dict_res.get, reverse=True)

        for i in range(k):

            res.append(sorted_keys[i])
           
        return res


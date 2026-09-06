import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        min_res = right
        while left <= right:
            mid = ( left + right ) // 2
            sum_rate = 0
            for pile in piles:
                sum_rate += math.ceil ( pile / mid )
            if sum_rate <= h:
                min_res  = mid
                right = mid -1
            else:
                left = mid + 1
        return min_res        

        
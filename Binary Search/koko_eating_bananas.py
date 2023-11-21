class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l,r = 1,max(piles)
        while l<=r:
            mid = l + (r-l)/2
            if self.canEatAll(piles,h,mid):
                r=mid-1
            else:
                l=mid+1
        return l

    def canEatAll(self,piles,h,mid):
        time = 0
        for pile in piles:
            time += pile/mid
            if pile%mid!=0:
                time+=1
        return time<=h
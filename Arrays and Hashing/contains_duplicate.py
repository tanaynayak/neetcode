class Solution(object):
    def containsDuplicate(self, nums):
        duplicate_set = set()

        for num in nums:
            if num in duplicate_set:
                return True
            duplicate_set.add(num)
        return False
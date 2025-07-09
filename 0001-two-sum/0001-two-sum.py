class Solution(object):
    def twoSum(self, nums, target):
        hmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            hmap[n] = i
        return
            


        
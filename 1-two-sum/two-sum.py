class Solution(object):
    def twoSum(self, nums, target):
        hmap = {}

        '''
        
        Logic: hmap is a dictionary storing values of number(n) and its respective index(i) as outlined below:
        
        Ex: nums = [3, 2, 4], target = 6

        hmap = {}

        i = 0 → n = 3 → diff = 3 → not in hmap → hmap = {3: 0}
        i = 1 → n = 2 → diff = 4 → not in hmap → hmap = {3: 0, 2: 1}
        i = 2 → n = 4 → diff = 2 → YES! 2 in hmap at index 1 → return [1, 2]
        
        '''

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            hmap[n] = i
        return
            


        
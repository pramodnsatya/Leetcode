class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
        ''' 
        n = len(nums)
        nums.sort()
        for i in range(0,n):
            if nums[i] == nums[i-1]:
                return True
        return False

        '''


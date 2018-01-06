'''
Created on Jan 5, 2018

@author: Jake
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        #make two pointers to hold one position, and check other position
        for x in range(len(nums)):
            for y in range(len(nums) - 1):
                y += 1
                #if the numbers add to targer and are the same index in array, return solution
                if(nums[x] + nums[y] == target and x != y):
                    arr.append(x)
                    arr.append(y)
                    return arr
        return("No such nums found in array")
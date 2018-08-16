"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            temp = target - nums[i]
            for j in range(i+1, len(nums)):
                if temp == nums[j]:
                    return [i,j]
                
       

def main():
	nums = [2, 7, 11, 15]
	target = 9
	obj = Solution()
	print(obj.twoSum(nums, target))

main()

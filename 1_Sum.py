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

        map = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in map:
                return [map[val], i]
            else:
                map[nums[i]] = i
        return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    print(obj.twoSum(nums, target))


main()

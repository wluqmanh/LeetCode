""""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def two_sum(self, nums, target):
    hashmap = {}
    for index, value in enumerate(nums):
        print('\nIndex: ', index, ', Value: ', value)
        key = target - value
        print('Key = %d - %d\n\t= %d' % (target, value, key))
        if key in hashmap:
            print('hashmap: ', hashmap)
            print('hashmap[%d]: %d' % (key, hashmap[key]))
            return [hashmap[key], index]
        else:
            hashmap[value] = index
            print('hashmap: ', hashmap)

nums = [11, 15, 6, 2, 7]
target = 9
two_sum(two_sum, nums, target)

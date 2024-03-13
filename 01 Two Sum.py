# https://leetcode.com/problems/two-sum/


def two_sum(self, nums, target):
    prevMap = {}
    
    for i, n in enumerate(nums):
        print('\ni: ', i, ', Value: ', n)

        diff = target - n
        print('Key = %d - %d\n\t= %d' % (target, n, diff))

        if diff in prevMap:
            print('prevMap: ', prevMap)
            print('prevMap[%d]: %d' % (diff, prevMap[diff]))
            return [prevMap[diff], i]
        
        prevMap[n] = i
        print('prevMap: ', prevMap)

nums = [11, 15, 6, 2, 7]
target = 9
two_sum(two_sum, nums, target)

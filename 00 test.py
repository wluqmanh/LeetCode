def two_sum(self, nums, target):
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in prev_map:
            print('prev_map[%d]: %d' % (diff, prev_map[diff]))
            return [prev_map[diff], i]

        prev_map[n] = i
        print('prev_map: ', prev_map)

nums = [11, 15, 6, 2, 7]
target = 9
two_sum(two_sum, nums, target)

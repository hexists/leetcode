#!/usr/bin/env python3

from typing import List
from pprint import pprint
from bisect import bisect_left 


'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum_v4(self, nums: List[int], target: int) -> List[int]:
        '''
        O(nlogn), use sorting
        '''
        def bsearch(a, x):
            i = bisect_left(a, x)
            return i if i != len(a) and a[i] == x else -1

        sorted_nums = sorted(nums)

        for i, snum in enumerate(sorted_nums):
            rest = target - snum
            fidx = bsearch(sorted_nums, rest)
            if fidx != -1:
                break

        if fidx != -1:
            ret = []
            for n, num in enumerate(nums):
                if snum == num:
                    ret.append(n)
                elif rest == num:
                    ret.append(n)

                if len(ret) == 2:
                    return ret
        return []

    def twoSum_v3(self, nums: List[int], target: int) -> List[int]:
        '''
        O(n), use dict(hash)
        '''
        vals = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in vals and i != vals[rest]:
                return [vals[rest], i]
            vals[num] = i
        return []

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        '''
        O(n), use dict(hash)
        '''
        vals = {}
        for i, num in enumerate(nums):
            vals[num] = i

        for i, num in enumerate(nums):
            rest = target - num
            if rest in vals and i != vals[rest]:
                return [i, vals[rest]]
        return []

    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        '''
        O(n^2)
        '''
        for i, num in enumerate(nums):
            rest = target - num
            for j in range(i + 1, len(nums)):
                if nums[j] == rest:
                    return [i, j]
        return []

if __name__ == '__main__':
    nums, target = [2, 7, 11, 15], 9
    # nums, target = [3, 2, 4], 6
    # nums, target = [3, 3], 6

    solution = Solution()
    ret = solution.twoSum_v3(nums, target)
    print(ret)

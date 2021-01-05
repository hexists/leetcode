#!/usr/bin/env python3


from typing import List

'''
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

ref:

https://www.pymoon.com/entry/540-Single-Element-in-a-Sorted-Array
https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.bsearch_single_value(nums, 0, len(nums) - 1)

    def bsearch_single_value(self, nums, start, end):
        if start >= end:
            return nums[start]

        mid = (start + end) // 2
        left = mid - 1
        right = mid + 1

        print('start = {}, end = {}'.format(start, end))
        print('mid = {}, left = {}, right = {}'.format(mid, left, right))
        print()

        if nums[left] == nums[mid]:
            if len(nums[start:left]) % 2 != 0:
                return self.bsearch_single_value(nums, start, left-1)
            else:
                return self.bsearch_single_value(nums, right, end)
        elif nums[mid] == nums[right]:
            if len(nums[right+1:end+1]) % 2 != 0:
                return self.bsearch_single_value(nums, right+1, end)
            else:
                return self.bsearch_single_value(nums, start, left)
        else:
            return nums[mid]


if __name__ == '__main__':

    nums = [1,1,2,3,3,4,4,8,8]  # 2
    # nums = [3,3,7,7,10,11,11]  # 10
    # nums = [1,1,2,3,3]  # 2
    # nums = [1,1,2,2,3]  # 3

    sol = Solution()
    ret = sol.singleNonDuplicate(nums)
    print(ret)

#!/usr/bin/env python3

import os
import sys
from typing import List
from pprint import pprint

'''
https://leetcode.com/problems/maximum-subarray/

53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
  Input: [-2,1,-3,4,-1,2,1,-5,4],
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
  If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Reference:
  https://m.blog.naver.com/PostView.nhn?blogId=dkdlelgksthf&logNo=221052887894&proxyReferer=https:%2F%2Fwww.google.com%2F
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0] if len(nums) > 0 else 0
        for i in range(1, len(nums)):
            if nums[i-1] + nums[i] < 0:
                nums[i] = 0
            elif nums[i-1] + nums[i] > nums[i]:
                nums[i] = nums[i-1] + nums[i]
            else:
                nums[i]

            # nums[i] = nums[i-1] + nums[i] if nums[i-1] + nums[i] > 0 and nums[i-1] + nums[i] > nums[i] else nums[i]

            max_val = max(nums[i], max_val)
        return max_val


if __name__ == '__main__':
    #example1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1]
    nums = [2, -3, 2, 3, 4, -5]
    nums = []
    nums = [-1, -3, -2]

    sol = Solution()
    ret = sol.maxSubArray(nums)
    print(ret)

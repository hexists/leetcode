#!/usr/bin/env python3

'''
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l, r = 1, x
        while True:
            m = (l + r) // 2

            if m == l or m == r:
                return m

            mm = m * m
            if mm > x:
                r = m
            elif mm < x:
                l = m
            else:
                return m


if __name__ == '__main__':
    x = 8
    x = 4
    x = 35

    sol = Solution()
    ret = sol.mySqrt(x)

    print('sqrt({}) = {}'.format(x, ret))

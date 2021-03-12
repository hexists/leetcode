#!/usr/bin/env python3

'''
50. Pow(x, n)
Medium

2181

3640

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        n, x = (n, x) if n > 0 else (n*-1, 1/x)

        count, reminder = 0, []
        while n > 1:
            reminder.append(n % 2)
            n //= 2
            count += 1
        # print('count    = {}'.format(count))
        # print('reminder = {}'.format(reminder))
        acc = x
        for c in range(count, 0, -1):
            acc = acc * acc
            if reminder[c-1] > 0:
               acc = acc * x 
        return acc

    # Time Limit Exceeded
    def myPow_timeout(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        acc = 1
        n, x = (n, x) if n > 0 else (n*-1, 1/x)
        for i in range(n):
            acc *= x
        return acc

if __name__ == '__main__':
    x_ns = [[2.0, 10],
            [2.1, 3],
            [2.0, -2],
            [2.0, 8],
            [2.0, 7],
            ]

    sol = Solution()

    for x, n in x_ns:
        xn = sol.myPow(x, n)
        print('x = {}, n = {}, pow(x, n) = {}'.format(x, n, xn))

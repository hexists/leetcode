#!/usr/bin/env python3


'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''


import os
import sys


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = list('()[]{}')
        pair = {'(': ')', '[': ']', '{': '}'}

        for val in list(s):
            if val not in valid:
                continue

            # print('stack     = {}'.format(stack))
            # print('val       = {}'.format(val))

            if len(stack) > 0 and stack[-1] in pair and pair[stack[-1]] == val:
                stack.pop()
            else:
                stack.append(val)

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # s = "()"  # True
    # s = "()[]{}"  # True
    s = "([)]"  # False
    s = "(){}}{"

    sol = Solution()
    ret = sol.isValid(s)
    print(ret)

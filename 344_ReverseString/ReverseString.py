#!/usr/bin/env python3


import os
import sys
from typing import List
from pprint import pprint


'''
https://leetcode.com/problems/reverse-string/
'''


class Solution:
    def reverseString_1st(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        j = len(s) - 1
        for i in range(j // 2 + 1):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            j -= 1

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        j = len(s) - 1
        for i in range(j // 2 + 1):
            s[i], s[j] = s[j], s[i]
            j -= 1

if __name__ == '__main__':
    ll = list('hello')

    sol = Solution()
    sol.reverseString(ll)

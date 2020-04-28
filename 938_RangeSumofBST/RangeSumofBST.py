#!/usr/bin/env python3

import os
import sys
from pprint import pprint

'''
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
  Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
  Output: 32

Example 2:
  Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
  Output: 23

Note:
  1. The number of nodes in the tree is at most 10000.
  2. The final answer is guaranteed to be less than 2^31.

참고:
  Solution을 보고 따라했음
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST_recursive(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

    def rangeSumBST_iterative(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans


if __name__ == '__main__':
    # Example 1
    bst = TreeNode(10)
    bst.left = TreeNode(5)
    bst.right = TreeNode(15)
    bst.left.left = TreeNode(3)
    bst.left.right = TreeNode(7)
    bst.right.right = TreeNode(18)

    L, R = 7, 15

    sol = Solution()
    ret = sol.rangeSumBST_recursive(bst, L, R)
    print('recursive solution result: {}'.format(ret))
    ret = sol.rangeSumBST_recursive(bst, L, R)
    print('iterative solution result: {}'.format(ret))

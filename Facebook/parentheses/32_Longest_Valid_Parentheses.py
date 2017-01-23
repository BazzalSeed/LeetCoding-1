"""
Description
____________
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


Approach
___________
"""


class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        maxlen = max(maxlen, i - start + 1)
                    else:
                        maxlen = max(maxlen, i - stack[-1])
        return maxlen

"""
Description
==============
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Approach
=========
Stack
Complexity
===========
One pass
"""


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for s_i in s:
            if len(stack) == 0 and s_i in [')', '}', ']']:
                return False
            elif len(stack) != 0 and self.isMatch(stack[-1], s_i):
                stack.pop()
            else:
                stack.append(s_i)
        return len(stack) == 0

    def isMatch(self, s1, s2):
        return (s1 == '(' and s2 == ')') or (s1 == '[' and s2 == ']') or (s1 == '{' and s2 == '}')

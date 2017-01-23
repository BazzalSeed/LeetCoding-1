"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""


class Solution(object):
    """
    If it's '(', either use it, or remove it.
    If it's '(', either use it, or remove it.
    Otherwise just append it.
    Lastly set StringBuilder to the last decision point.

    """

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set([])
        rmL, rmR = 0, 0
        cur = []
        for i in s:
            if i == '(':
                rmL += 1
            if i == ')':
                if rmL != 0:
                    rmL -= 1
                else:
                    rmR += 1
        self.DFS(res, s, 0, rmL, rmR, 0, cur)
        return list(res)

    def DFS(self, res, s, i, rmL, rmR, open, cur):
        if i == len(s) and rmL == 0 and rmR == 0 and open == 0:
            res.add(''.join(cur))
            return
        if i == len(s) or rmL < 0 or rmR < 0 or open < 0:
            return
        char = s[i]

        if char == '(':
            # Remove it
            self.DFS(res, s, i + 1, rmL - 1, rmR, open, cur)
            self.DFS(res, s, i + 1, rmL, rmR, open + 1, cur + [char])
        elif char == ')':
            self.DFS(res, s, i + 1, rmL, rmR - 1, open, cur)
            self.DFS(res, s, i + 1, rmL, rmR, open - 1, cur + [char])
        else:
            self.DFS(res, s, i + 1, rmL, rmR, open, cur + [char])

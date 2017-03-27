"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

Approach
_____________

dfs
+++++
Limit max removal rmL and rmR for backtracking boundary.
Otherwise it will exhaust all possible valid substrings, not shortest ones.
 Scan from left to right, avoiding invalid strs (on the fly) by checking num of open parens.

If it's '(', either use it, or remove it.
If it's '(', either use it, or remove it.
Otherwise just append it.

pruning DFS by
if open < 0 or rmL < 0 or rmR < 0 or i > len(s) - 1:
    return


Maintain

rmL - remaning '(' shuold be removed for the optimal solution
rmR - reminaing ')' should be removed for the optimal solution
open - number of open '(' that did not closed by ')'
path ,result

Base

if open == 0 and rmL == 0 and rmR == 0 and len(s) == i:
    result.add(path)
    # return
if open < 0 or rmL < 0 or rmR < 0 or i > len(s) - 1:
    return

Complexity
_____________
"""


class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rmL, rmR = 0, 0
        for i in s:
            if i == '(':
                rmL += 1
            elif i == ')':
                if rmL > 0:
                    rmL -= 1
                else:
                    rmR += 1
        result = set([])
        self.dfs(result, s, 0, rmL, rmR, 0, "")
        return list(result)

    def dfs(self, result, s, i, rmL, rmR, open, path):
        if open == 0 and rmL == 0 and rmR == 0 and len(s) == i:
            result.add(path)
            # return
        if open < 0 or rmL < 0 or rmR < 0 or i > len(s) - 1:
            return
        char = s[i]
        if char == '(':
            self.dfs(result, s, i + 1, rmL - 1, rmR, open, path)
            self.dfs(result, s, i + 1, rmL, rmR, open + 1, path + char)
        elif char == ')':
            self.dfs(result, s, i + 1, rmL, rmR - 1, open, path)
            self.dfs(result, s, i + 1, rmL, rmR, open - 1, path + char)
        else:
            self.dfs(result, s, i + 1, rmL, rmR, open, path + char)

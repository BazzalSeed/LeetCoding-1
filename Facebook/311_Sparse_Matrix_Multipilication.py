"""
Description
___________
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |


Approach
_______________
very naive. Just avoid calculation when A[i][j] or B[j][k] is zero
"""


class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if (A == None or B == None):
            return -1

        I = len(A)
        J = len(A[0])
        K = len(B[0])
        result = [[0 for _ in xrange(K)] for _ in xrange(I)]
        for i in xrange(I):
            for j in xrange(J):
                if A[i][j] != 0:
                    for k in xrange(K):
                        if B[j][k] != 0:
                            result[i][k] += A[i][j] * B[j][k]
        return result

"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

Approach
________________
Remember the level order traversal?
0. on the queue use tuple (column_order, node)
1. use queue to BFS
2. use a map to map column_order->value
3. left -1 to column_order, right +1 to column_order
4. return map.values

extra: dict is not ordered use sorted in the end


Complexity
_______________________
sorting : O(2^h)
BFS : O(m) = O(n)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        dic = {}
        q = []
        new_root = (0, root)
        q.insert(0, new_root)
        while q:
            current_node = q.pop()
            node = current_node[1]
            column_order = current_node[0]
            if dic.has_key(column_order):
                dic[column_order].append(node.val)
            else:
                dic[column_order] = [node.val]
            if node.left:
                q.insert(0, (column_order - 1, node.left))
            if node.right:
                q.insert(0, (column_order + 1, node.right))

        return [i[1] for i in sorted(dic.items())]

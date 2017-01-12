"""
Description
___________
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Approach
________
http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


So for this problem we are tasked with finding the next element that would come
after the target node, p. In order to do this we take advantage of the Binary
Search Tree property. This property states that for a parent node all children to
the left of that node will have a value that is less than it, and all right children
will have a value greater than it.
http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/binarySearchTree.html

There are two situations that can occur in this problem.

1) The current node has a right tree: return the left-most node of the right tree.
2) Doesn't have a right tree:
    a) Returns the parent node. (Implement Binary Search updating parent only when we go left)
    b) Returns null.

Complexity
__________

For a balanced tree O(lg(n)), unbalanced O(H)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        # write your code here
        if root == None or p == None:
            return None

        # When right tree not empty
        if p.right != None:
            p = p.right
            while (p.left != None):
                p = p.left
            return p

        else:
            parent_successor = None

            while root.val != p.val and root != None:
                if p.val > root.val:
                    root = root.right
                else:
                    parent_successor = root
                    root = root.left
            return parent_successor

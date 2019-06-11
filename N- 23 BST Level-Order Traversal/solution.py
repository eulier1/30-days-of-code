
/**
* I have submit the whole exercices and the solution
* due lack of BSF implementations in python for BST
*/

import sys
from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = deque([root]) if root else deque([])
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

T=[3,5,4,7,2,1]
myTree=Solution()
root=None
for data in T:
    root=myTree.insert(root,data)
myTree.levelOrder(root)
def height(self,node):
  if node is None:
    return -1
  else:
    return sum(self.height(node.left), self.height(node.right)) + 1

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Tree:
    def __init__(self,val):
        self.root = TreeNode(val)
    def insert(self,val):
        def insert_node(root,val):
            if root.val > val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    insert_node(root.left,val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    insert_node(root.right,val)
        insert_node(self.root,val)

    def search(self,val) -> bool:
        def search_val(root,val)->bool:
            if not root:
                return False
            if root.val < val:
                 return search_val(root.right, val)
            return search_val(root.left,val)
        return search_val(self.root,val)
    
tree = Tree(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print(tree.search(4))
print(tree.search(9))
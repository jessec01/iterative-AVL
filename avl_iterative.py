from node import Node 
class AVLIterativo:
    def __init__(self):
        self.count =  0
        self.root = None
    def insert_public(self,node):
        self.insert(self.root,node)
    def insert(self,root,node_new):
        node_now = self.root
        node = None
        while not node_now is None:
            node = node_now
            if node_new.x<node_now.x:
                node_now = node_now.left
            else:
                node_now = node_now.right
        node_new.parent = node_now
        if node is None:
            self.root = node_new
        elif node_new.x < node.x:
            node.left = node_new
        else:
            node.right = node_new
    def search(self ,key):
        return self.tree_search(self.root,key)
    def tree_search(self,root,k):
        node=root        
        while not node is None and k != node.x:
            if k<node.x:
                node = node.left
            else:
                node=node.right
        return node
    def maximun_tree(self,node_aux):
        node = node_aux 
        while not node.right is None:
            node = node.right
        return node
    def minimun_tree(self,node_aux):
        node = node_aux
        while not node.left is None:
            node = node.left
        return node
    def tree_sucesor(self,node):
        if not node is None:
            return self.minimun_tree(node.rigth)
        node_now=node.parent()
        while not node_now is None and node == node_now.right:
            node = node_now
            node_now = node_now.parent       
    def tree_predecesor(self,node):
        if not node is None:
            return self.minimun_tree(node.left)
        node_now=node.parent
        while not node_now is None and node == node_now.left:
            node = node_now
            node_now = node_now.parent
    def inorden(self):
        self.morris_inorden(self.root)
    def morris_inorden(self,root): 
        # Set current to root of binary tree 
        curr = root
        while(curr is not None):
            if curr.left is None:
                print(curr.x)
                curr = curr.right
            else: 
			    # Find the previous (prev) of curr
                prev = curr.left
                while(prev.right is not None and prev.right != curr):
                    prev = prev.right
                # Make curr as right child of its prev 
                if(prev.right is None):
                    prev.right = curr
                    curr = curr.left 
				# fix the right child of prev
                else:
                    prev.right = None
                    print(curr.x)
                    curr = curr.right
avl = AVLIterativo()
node = Node(4)
avl.insert_public(node)
node = Node(5)
avl.insert_public(node)
node = Node(2)
avl.insert_public(node)
node = Node(1)
avl.insert_public(node)
node = Node(3)
avl.insert_public(node)
avl.inorden()

print(avl.search(5).x)
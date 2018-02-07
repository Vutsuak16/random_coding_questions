class Node:
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None




def insert(root,val):
	new_node=Node(val)
	if root==None:
		root=new_node
	else:
		node=root
		while True:
			if val<node.value:
				if node.left==None:
					node.left=new_node
					break
				node=node.left
			else:
				if node.right==None:
					node.right=new_node
					break
				node=node.right
		return node


def get_height(root):
	if root==None:
		return -1
	return max(get_height(root.left),get_height(root.right))+1

def is_balanced(root):
	if root==None:
		return True
	else:
		
		height_diff=get_height(root.left)-get_height(root.right)
		if abs(height_diff)>1:
			return False
		else:
			return is_balanced(root.left) and is_balanced(root.right)
		


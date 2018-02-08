class Node:

	def __init__(self,value):

		self.value=value
		self.left=None
		self.right=None

def create_tree(start,end,arr):
	if start>end:
		return ''
	else:
		mid=(start+end)//2
		root=Node(arr[mid])
		root.left=create_tree(start,mid,arr)
		root.right=create_tree(mid+1,len(arr)-1,arr)
		return root

def array_to_tree(arr):
	create_tree(0,len(arr)-1,arr)

def inorder(self,root):
	if root==None:
		return None
	else:
		inorder(root.left)
		print(root.value)
		inorder(root.right)

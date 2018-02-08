class  Node():
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None



def get_height(r):
	if r==None:
		return 0
	return max(get_height(r.left),get_height(r.right))+1


def print_level(r,level):
	if r==None:
		return None
	if level==1:
		print(r.value,end=" ")

	elif level>1:
		print()
		print_level(r.left,level-1)
		print_level(r.right,level-1)

def print_level_order(root):
	height=get_height(root)
	for i in range(1,height+1):
		print_level(root,i)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(4)
root.left.right.right = Node(41)
 
print_level_order(root)
class Node:
	def __init__(self,val):
		self.value=val
		self.next=None


def add(head,value):
	node=Node(value)
	curr=head
	while curr.next is not None:
		curr=curr.next
	curr.next=node

def get_add(head,value):

	curr=head
	while curr.value != value:
		if curr.next ==None:
			return 0
		curr=curr.next
	return curr

def print_list(head):
 	curr=head
 	while curr.next is not None:
 		print(str(curr.value)+"-->",end="")
 		curr=curr.next
 	print(str(curr.value))

def remove(head,n):
	curr=head
	while curr.next.value!=n.value:
		curr=curr.next
	curr.next=curr.next.next
	print_list(head)

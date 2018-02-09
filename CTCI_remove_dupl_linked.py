class Node:
 	def __init__(self,val):
 		self.value=val
 		self.next=None


def add(head,val):
 	node=Node(val)
 	curr=head
 	while curr.next is not None:
 		curr=curr.next
 	curr.next=node


def print_list(head):
 	curr=head
 	while curr.next is not None:
 		print(str(curr.value)+"-->",end="")
 		curr=curr.next
 	print(str(curr.value))

def remove_duplicates(head):

 	print_list(head)

 	l={}
 	
 	curr=head
 	prev=head
 	while curr is not None:
 		if curr.value in l:
 			prev.next=curr.next
 		else:
 			l[curr.value]=True
 		prev=curr
 		curr=curr.next
 	print_list(head)


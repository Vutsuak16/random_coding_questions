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


def nth_to_last(head,n):

	curr=head
	length=0
	while curr is not None:
		length+=1
		curr=curr.next

	curr=head
	index=length-1-n
	if index<0:
		return "index out of bounds"

	else:
		while index>=0:
			prev=curr
			curr=curr.next
			index-=1

	print(prev.value)
	return 
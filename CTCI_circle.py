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
 	return node


def circle(head):

	prev=head
	curr=head.next
	while True:
		if curr==None or prev==None or curr.next==None:
			return "No circle"
		if prev.value==curr.value:
			return prev.value
		curr=curr.next.next
		prev=prev.next


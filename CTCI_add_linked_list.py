class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

def add(head,value):

	node=Node(value)
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


def add_lists(head1,head2):

	print_list(head1)
	print_list(head2)

	if head1 == None and head2==None :
		return None

	if head1== None:
		print_list(head2)
		return 

	if head2==None:
		print_list(head1)
		return

	carry=0
	num=0
	curr1=head1
	curr2=head2
	head3=None
	flg=0
	while curr1 is not None and curr2 is not None:
		num=curr1.value+curr2.value+carry
		if num//10 ==0:
			carry=0

		else:
			carry=num%10
			if carry==0:
				carry=1
			num=num-10
		if flg==0:
			head3=Node(num)
			flg=1
		else:
			add(head3,num)

		curr1=curr1.next
		curr2=curr2.next

	print_list(head3)
class Stack:

	def __init__(self):
		self.stack=[]

	def size(self):
		return len(self.stack)


	def pop(self):
		if self.size()==0:
			return "Stack is empty"
		else:
			self.stack.pop()

	def print_stack(self):
		for i in self.stack[::-1]:
			print(i)

	def push(self,value):
		self.stack.append(value)

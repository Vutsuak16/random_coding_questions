def reverse(string):
	
	if len(string)==0 or len(string)==1 or len(string)==2:
			
			return string
		
	new_string=""

	for i in range(len(string)-2,-1,-1):
		new_string+=string[i]
		
	new_string+="\0"

	return new_string


print(reverse("100"+"\0"))
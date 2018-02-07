def rep_lace(string,s):
	string=list(string)
	for i in range(len(string)):
		if string[i]==" ":
			string[i]=s
	return "".join(string)

print(rep_lace("a a a a n","%20"))
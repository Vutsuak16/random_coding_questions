def check_duplicate(string):
	
	if len(string)==0 or len(string)==1:
		return True
	l=string
	ct=0
	flg=True
	for i in range(len(l)):
		character=l[i]
		for j in range(len(l)):
			if j==i:
				continue
			else:
				if l[j]==character:
					ct+=1
		if ct>=1:
			flg=False
			break
		else:
			ct=0
	return flg

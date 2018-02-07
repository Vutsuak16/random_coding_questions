def remove_duplicate(string):
	
	if len(string)==0 or len(string)==1:
		return string
	bin_hash=[0]*256
	l=list(string)
	res_index=0
	mov_index=0
	temp=''
	while mov_index != len(l):
		temp=l[mov_index]
		if bin_hash[ord(temp)]==0:
			bin_hash[ord(temp)]=1
			l[res_index]=l[mov_index]
			res_index+=1
		mov_index+=1
	return "".join(l[0:res_index])

	


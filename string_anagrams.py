def anagrams(s1,s2):

	if len(s1)==0 and len(s2)==0:
		return True
	if len(s1)==0 and len(s2) !=0 or len(s1) != 0 and len(s2) ==0:
			return False
	bin_hash_1=[0]*256
	bin_hash_2=[0]*256
	for i in s1:
		bin_hash_1[ord(i)]+=1
	for i in s2:
		bin_hash_2[ord(i)]+=1
	for i in range(256):
		if bin_hash_1[i] != bin_hash_2[i]:
			return False

	return True

#print(anagrams("awdadadw","wwaaaddd"))
		


def anagrams(s1,s2):

	if len(s1)==0 and len(s2)==0:
		return True
	if len(s1)==0 and len(s2) !=0 or len(s1) != 0 and len(s2) ==0:
			return False
	if sorted(s1)==sorted(s2):
		return True
	else:
		return False

print(anagrams("awdadadw","wwaaaddd"))
		


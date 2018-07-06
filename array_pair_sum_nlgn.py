
def array_pair(array , k):

	if len(array) < 2:
		return

	array = sorted(array) #nlgn


	left , right = 0 , len(array)-1


	while left < right:

		current_sum = array[left] + array[right]

		if current_sum == k:
			print(array[left] , array[right])
			left += 1                          #iterator movement

		elif current_sum < k:
			left += 1

		else:
			right -= 1 


array = [4 , 5 , -1 , 0 , 1 , 4 , 5 , 9 , 11 , 50 , 8]
k = 9

array_pair(array , k)
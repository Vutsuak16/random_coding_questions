def array_pair_sum_n(arr , k):

	s = set()

	for i in arr:

		temp = k - i

		if temp >= 0 and temp in s:

			print(i , temp)

		s.add(i)


array = [4 , 5 , -1 , 0 , 1 , 4 , 5 , 9 , 11 , 50 , 8]
k = 9

array_pair_sum_n(array , k)
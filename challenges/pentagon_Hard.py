def pentagonal(num):
	total = 1
	for x in range(2, num+1):
		total += (x-1)*5
	return total
def number_length(num):
	if num<10:
		return 1
	counter = 0
	while(num>=10):
		num = num // 10
		counter += 1
	return counter +1
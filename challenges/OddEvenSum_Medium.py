def sum_odd_and_even(lst):
	listeven = [x for x in lst if x%2==0]
	listodd = [x for x in lst if x%2==1]
	return [sum(listeven), sum(listodd)]
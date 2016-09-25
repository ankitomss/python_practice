def calculate_sum(select, list_int):
	summ=0
	for i in range(len(select)):
		if(select[i]==1):
			summ=summ+list_int[i]

	return summ

def check_solution(list_int, cur_position, selected, select, min_diff):
	
	if(cur_position>= len(list_int)):
		return min_diff;

	if(selected>len(list_int)/2):
		return min_diff;
	
	summ=0
	for i in range(len(list_int)):
		summ=summ+list_int[i]

	
	
	min_diff=check_solution(list_int, cur_position+1, selected, select, min_diff)

	select[cur_position]=1
	selected = selected+1
#	print "outside the loop need to check what is selected here", select, selected
	calculated_diff=0
	if(selected == len(list_int)/2):
#		print "need to check what is selected here", select, calculate_sum(select, list_int), summ
		calculated_diff =  abs(summ - 2*calculate_sum(select, list_int))
		print "calculated diff is", calculated_diff, min_diff
		if(calculated_diff < min_diff):
			min_diff = calculated_diff
			print "now element is ", select
			print "min diff is", min_diff
	else:
			min_diff=check_solution(list_int, cur_position+1, selected, select, min_diff)
	
	select[cur_position]=0
	return min_diff




list_int = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
select=[0,0,0,0,0,0,0,0,0,0,0]
min_diff=1000
min_diff=check_solution(list_int,0,0,select,min_diff)
print "now element is ", select
print "min_diff is", min_diff



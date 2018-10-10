# import numpy as np
# l=[0,0,0,2,5,7,1,0,7,5]
# for i in range(len(l)):
	# if l[i]!=0:
		# print(l[i:])
		# break
# z=list("".join([str(x) for x in l]).lstrip('0'))
# print(z)
# ne=np.trim_zeros(l,'f')
# print(ne)
# old_list = [0, 0, 1, 2,3.5,'dsa',0, 3, 0]
# string = ''.join([str(x) for x in old_list])
# string = string.lstrip('0')
# new_list = [int(character) for character in string]
# print(new_list)
# [print(l[i:]) for i in range(len(l))[:None if l[i]==0 else l[i].index()]]
[ 'buzz' if x != 'fizz' and x != 'fizzbuzz' and x%5 == 0 else x for x in 

	['fizz' if x != 'fizzbuzz' and x%3 == 0 else x for x in 
[ 'fizzbuzz' if x % 3 == 0 and x % 5 == 0 else x for x in range(1,101) ]]]
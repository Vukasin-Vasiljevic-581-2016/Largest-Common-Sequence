#!/bin/env python

def sub_sequence(st1,st2):
	"""
		Finding biggest subsequence in string1 and string2 in order
		Examples:
			 * 'ABCABA' , 'ABBA' --> 'ABBA'
			 * 'aaaaa' , 'aa' --> 'aa'
			 * 'AGGTAB' , 'GXTXAYB' --> 'GTAB'
			 * 'ABAZDC' , 'BACBAD' --> 'ABAD'		
	"""
	
	# creating two list with elements of string
	st1 = list(st1)
	st2 = list(st2)
	res1 = []
	res2 = []
	# determining which string is longer
	if (len(st1) <= len(st2)):
		lower = st1
		bigger = st2
	else:
		lower = st2
		bigger = st1
	
	# for each element in shorter string go throug each element in longer string
	# and check in other for loop check if there is occurence in longer string 
	index = 0
	for j in range(0,len(lower)+1): # go for every element

		for i in lower[j:]:	# everytime start with next element
			if i in bigger[index:]:
				res1.append(i)	
				index = (bigger[index:]).index(i) # start next time from index of found element
		index = 0
		for i in res1: # check if every element in result has the same occurence in both strings
			if(res1.count(i)>lower.count(i) or res1.count(i)>bigger.count(i)):
				res1=[]	
		# check if new result is longer than old one, if so, update old one with new and new set to ''	
		if (len(res1)>=len(res2)):
			res2=res1
			res1 = []
		else:
			res1=[]
	# megre list in string	
	res = ''
	for i in res2:
		res+=i
	return res
			
		
			

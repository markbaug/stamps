def stamps (number):
	five=0
	two=0
	one=0
	while number>=5:
		five=five+1
		number=number-5
	while number>=2:
		two=two+1
		number=number-2
	while number>=1:
		one=one+1
		number=number-1
	return five,two,one
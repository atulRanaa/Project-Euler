p = [2,3,5,7,11,13,17]
for i in range(1023456789,9876543211):
	s = set([c for c in str(i)])
	if len(s) == 10:
		num = str(i)
		f = True
		for i in range(1,8):
			if int(num[i:(i+3)])%p[i-1] != 0:
				f = False
				break
		if f:
			print i
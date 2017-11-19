s = [0]*1000001
for i in range(1,801):
	num = i*(3*i-1)/2
	s[num] = 1
l = len(s)
print l
for i in range(l):
	for j in range((i+1),l):
		if s[(s[j]+s[i])] == 1 and s[(s[j]-s[i])]==1:
			print s[j],s[i]
			break

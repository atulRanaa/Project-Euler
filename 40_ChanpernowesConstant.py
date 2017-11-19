s = ""
i = 1
while len(s) <= 1000000:
	s += str(i)
	i += 1
print s[0]
print s[9]
print s[99]
print s[999]
print s[9999]
print s[99999]
print s[999999]
print s[:20]
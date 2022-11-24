a,b = 1,3
i = 5
while i <16:
	print (a-1, end = ";")
	a += i**3+i*2+b*i
	b += 1
	i+=1
print (a)

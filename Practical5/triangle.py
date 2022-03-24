#a is the total number of dots in each picture
#b is the number of dots in the last row in each picture
#a,b both start from 1
a=1
b=1
#b increases by 1 in each picture
#a(this time)=a(last time)+b(this time)
for b in range (1,11):
	print(a)
	b=b+1
	a=a+b

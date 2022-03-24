#a is the total number of pieces.
#b is the total number of newly added pieces. b increases by 1 in each picture.
#a(this time)=a(last time)+b
#a starts from 1, b starts from 0.
a=1
b=0
while a<64:
	print(b)
	b=b+1
	a=a+b
	if b==11:
		print(b,a)
		if a>=64:
			print('When we have applied 12 straight cuts, there will be 67 pieces of pizza,which is enough for every student in IBI1')
#Program finished! Let's enjoy our pizza! (crunch crunch crunch...)

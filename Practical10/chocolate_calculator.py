a=int(input('Total money: '))
b=int(input('Price of one chocolate bar: '))

def chocolate():
	bars=a//b
	rem=a%b
	print('I can buy '+str(bars)+' chocolate bars.')
	print('The change left over is '+str(rem)+'.')
	return(a,b)

print(chocolate())	

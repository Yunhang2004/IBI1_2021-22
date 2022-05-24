from fractions import Fraction
DNA=input('DNA sequence: ')
#Process sequences with both upper and lower cases
DNA=DNA.upper()

def dna_calculator(DNA):
	"""
	Input: DNA strand
	Returns the proportion of A, T, C, G
	"""
	L=len(DNA)
	a=DNA.count('A')
	b=DNA.count('T')
	c=DNA.count('C')
	d=DNA.count('G')
	print('The proportion of A is '+str(Fraction(a,L)))
	print('The proportion of T is '+str(Fraction(b,L)))
	print('The proportion of C is '+str(Fraction(c,L)))
	print('The proportion of G is '+str(Fraction(d,L)))

print(dna_calculator(DNA))	





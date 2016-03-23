def dodawanie(a,b):
	return a + b
try:	
	a=int(input("Podaj pierwsza liczbe "))	
	b=int(input("Podaj druga liczbe "))
	print(dodawanie(a,b))
except ValueError as ve:
	print('wprowadzono bledne dane, koniec')
input()
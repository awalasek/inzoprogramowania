def dodawanie(a,b):
	return a + b

def get_info():
	return "To jest program kalkulator stworzony przeze mnie i nikogo innego"

try:	
	a=int(input("Podaj pierwsza liczbe "))	
	b=int(input("Podaj druga liczbe "))
	print(dodawanie(a,b))
except ValueError as ve:
	print('wprowadzono bledne dane, koniec')
print(get_info())	
input()
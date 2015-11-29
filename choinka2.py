a = input ('Podaj liczbę gwiazdek ')
a = int (a)
b = '*'
def choinka (z):
	for c in range (1,2*z,2):
		print ((b*c).center(2*z-1))
choinka (a)
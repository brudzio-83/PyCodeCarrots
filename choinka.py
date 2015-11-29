a = input ('Podaj liczbę gwiazdek ')
a = int (a)
b = 'x'
for c in range (1,2*a,2):
	print ((b*c).center(2*a-1))
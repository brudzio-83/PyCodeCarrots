x = input ('podaj plec k-kobieta m-mezczyzna ')
waga = input ('podaj  wagę (w kg) ')
wzrost = input ('podaj wzrost (w m) ')
waga = float (waga)
wzrost = float (wzrost)
BMI = waga / (wzrost**2)
print ('Twoje BMI wynosi %.2f' % (BMI,))
if x == 'k':
	if BMI < 17.5:
		print ('niedowaga')
	elif BMI < 22.0:
		print ('normalna waga')
	elif BMI < 25.0:
		print ('niedowaga')
	else:
		print ('nadwaga')
elif x == 'm':
	if BMI < 18.8:
		print ('niedowaga')
	elif BMI < 25.0:
		print ('normalna waga')
	elif BMI < 30.0:
		print ('niedowaga')
	else:
		print ('nadwaga')

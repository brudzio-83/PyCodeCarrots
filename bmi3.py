waga = input ('podaj  wagę ')
wzrost = input ('podaj wzrost w metrach ')
waga = float (waga)
wzrost = float (wzrost)
BMI = waga / (wzrost**2)
print ('Twoje BMI wynosi ' + str (BMI))
print ('Twoje BMI wynosi ', BMI)
if BMI < 18.5:
	print ('niedowaga')
elif BMI < 25.0:
	print ('normalna waga')
elif BMI < 30.0:
	print ('niedowaga')
else:
	print ('nadwaga')
class człowiek:
	waga = 0
	wiek = 0

	def jesc (self):
		self.waga = self.waga + 10
	def wiek (self):
		self.wiek = self.wiek + 10


ala = człowiek ()
ala.waga = 50
ala.wiek = 20
print (ala.waga)
print (ala.wiek)

aga = człowiek ()
aga.waga = 45
aga.wiek = 30
print (aga.waga)
print (aga.wiek)

ala.jesc ()
print (ala.waga)

aga.jesc ()
print (aga.waga)



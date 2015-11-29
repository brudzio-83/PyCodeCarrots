class człowiek:
	waga = 0
	wiek = 0

	def jesc (self):
		self.waga = self.waga + 10
	def wiek (self):
		self.wiek = self.wiek + 10


aga = człowiek ()
aga.waga = 45
aga.wiek = 30

print (aga.waga)
print (aga.wiek)

aga.jesc ()
print (aga.waga)
print (aga.waga)
from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Rys import Rys
from Organisms.Antylopa import Antylopa
import os
import random


if __name__ == '__main__':
	pyWorld = World(10, 10)

	newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Rys(position=Position(xPosition = 5, yPosition=5), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Antylopa(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	plaga = False
	counter = 0

	for _ in range(0, 50):
		print("\nWybierz czynność:\n(1) Tryb Plagi\n(2) Dodawanie Organizmu\n(3) Następna Tura\n(4) Zakończ Program")
		wybor = int(input("Wybór: "))
		if wybor == 1:
			plaga = True
			counter = 2 #Czas plagi 2 tury
		elif wybor == 2:
			while 1:
				wybrana_pozycja = [0, 0]
				wybrana_pozycja[1] = int(input("X: "))
				wybrana_pozycja[0] = int(input("Y: "))
				pozycja = Position(xPosition=wybrana_pozycja[1], yPosition=wybrana_pozycja[0])
				if pyWorld.positionOnBoard(pozycja) and pyWorld.getOrganismFromPosition(pozycja) is None:
					orgsign = input("Organizm(Znak): ")
					if orgsign == "G":
						pyWorld.addOrganism(Grass(position=pozycja, world=pyWorld))
					elif orgsign == "A":
						pyWorld.addOrganism(Antylopa(position=pozycja, world=pyWorld))
					elif orgsign == "R":
						pyWorld.addOrganism(Rys(position=pozycja, world=pyWorld))
					elif orgsign == "S":
						pyWorld.addOrganism(Sheep(position=pozycja, world=pyWorld))
				else:
					print("Wybrano zajętą lub błędną pozycję!\n")
				os.system('cls')
				print(pyWorld)
				inp = input("")
				break
		elif wybor == 4:
			break



		if (counter > 0): #Upływanie czasu plagi
			counter -= 1
		else:
			plaga = False

		os.system('cls')
		pyWorld.makeTurn(plaga)
		print(pyWorld)

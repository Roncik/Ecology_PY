import pytest

from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Rys import Rys
from Organisms.Antylopa import Antylopa

class Testy_Rys:

    def test_atrybuty(self):
        pyWorld = World(10, 10)
        initrys = Rys(position=Position(xPosition=0, yPosition=0), world=pyWorld)
        assert initrys.power == 6 and initrys.initiative == 5 and initrys.liveLength == 18 and initrys.powerToReproduce == 14 and initrys.sign == 'R'


class Testy_Antylopa:

    def test_atrybuty(self):
        pyWorld = World(10, 10)
        initantylopa = Antylopa(position=Position(xPosition=0, yPosition=0), world=pyWorld)
        assert initantylopa.power == 4 and initantylopa.initiative == 3 and initantylopa.liveLength == 11 and initantylopa.powerToReproduce == 5 and initantylopa.sign == 'A'

    def test_ucieczka(self):
        pyWorld = World(10, 10)
        initantylopa = Antylopa(position=Position(xPosition=1, yPosition=0), world=pyWorld)
        pyWorld.addOrganism(initantylopa)
        initrys = Rys(position=Position(xPosition=0, yPosition=0), world=pyWorld)
        pyWorld.addOrganism(initrys)
        pyWorld.makeTurn(False)
        assert initantylopa.position.x == 3 and initantylopa.position.y == 0

    def test_atak(self):
       pyWorld = World(10, 10)
       initantylopa = Antylopa(position=Position(xPosition=0, yPosition=0), world=pyWorld)
       pyWorld.addOrganism(initantylopa)
       initrys = Rys(position=Position(xPosition=1, yPosition=0), world=pyWorld)
       pyWorld.addOrganism(initrys)
       pyWorld.makeTurn(False)
       assert len(pyWorld.organisms) == 1


class Testy_Plaga:

    def test_plaga(self):
        pyWorld = World(10, 10)
        init_Antylopa = Antylopa(position=Position(xPosition=1, yPosition=1), world=pyWorld)
        init_Rys = Rys(position=Position(xPosition=1, yPosition=0), world=pyWorld)
        init_Owca = Sheep(position=Position(xPosition=2, yPosition=0), world=pyWorld)
        init_Trawa = Grass(position=Position(xPosition=3, yPosition=0), world=pyWorld)
        pyWorld.addOrganism(init_Antylopa)
        pyWorld.addOrganism(init_Rys)
        pyWorld.addOrganism(init_Owca)
        pyWorld.addOrganism(init_Trawa)
        livelA = init_Antylopa.liveLength * 0.5 - 1
        livelR = init_Rys.liveLength * 0.5 - 1
        livelO = init_Owca.liveLength * 0.5 - 1
        livelT = init_Trawa.liveLength * 0.5 - 1
        pyWorld.makeTurn(True)
        assert livelA == init_Antylopa.liveLength and livelR == init_Rys.liveLength and livelO == init_Owca.liveLength and livelT == init_Trawa.liveLength

class Testy_Dodawanie:

    def test_dodanie_jeden_na_drugi(self):
        pyWorld = World(10, 10)
        pozycja = Position(xPosition=1, yPosition=2)
        if pyWorld.positionOnBoard(pozycja) and pyWorld.getOrganismFromPosition(pozycja) is None:
            pyWorld.addOrganism(Sheep(position=pozycja, world=pyWorld))
        if pyWorld.positionOnBoard(pozycja) and pyWorld.getOrganismFromPosition(pozycja) is None:
            pyWorld.addOrganism(Rys(position=pozycja, world=pyWorld))
        assert pyWorld.getOrganismFromPosition(pozycja).sign == "S"

    def test_dodanie_poza_swiat(self):
        pyWorld = World(10, 10)
        pozycja = Position(xPosition=10, yPosition=2)
        if pyWorld.positionOnBoard(pozycja) and pyWorld.getOrganismFromPosition(pozycja) is None:
            pyWorld.addOrganism(Sheep(position=pozycja, world=pyWorld))
        assert pyWorld.getOrganismFromPosition(pozycja) is None


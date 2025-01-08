from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
from Position import Position
import random


class Animal(Organism):

	def __init__(self, animal=None, position=None, world=None):
		super(Animal, self).__init__(animal, position, world)
		self.__lastPosition = position

	@property
	def lastPosition(self):
		return self.__lastPosition

	@lastPosition.setter
	def lastPosition(self, value):
		self.__lastPosition = value

	def move(self):
		result = []
		pomPositions = self.getNeighboringPosition()
		newPosition = None
		
		if self.sign == 'A': #Zachowanie Antylopy
			pomPos2 = self.getNeighboringPositionNoFilter()
			for pos in pomPos2:
				closeOrganism = self.world.getOrganismFromPosition(pos)
				if closeOrganism is not None:
					if closeOrganism.sign == 'R':
						newPositionX = self.position.x
						newPositionY = self.position.y
						newPosition = Position(xPosition=newPositionX, yPosition=newPositionY)
						diffX = self.position.x - pos.x
						diffY = self.position.y - pos.y
						if diffX == 1:
							newPosition.x += 2
						elif diffX == -1:
							newPosition.x -= 2
						if diffY == 1:
							newPosition.y += 2
						elif diffY == -1:
							newPosition.y -= 2
						
						if self.world.positionOnBoard(newPosition) and self.world.getOrganismFromPosition(newPosition) is None:
							result.append(Action(ActionEnum.A_RUN, newPosition, 0, self))
						else:
							result = closeOrganism.consequences(self)
						return result
						

		

		if pomPositions:
			newPosition = random.choice(pomPositions)
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			self.lastPosition = self.position
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None:
				result.extend(metOrganism.consequences(self))
		return result

	def action(self):
		result = []
		newAnimal = None
		birthPositions = self.getNeighboringBirthPosition()

		if self.ifReproduce() and birthPositions:
			newAnimalPosition = random.choice(birthPositions)
			newAnimal = self.clone()
			newAnimal.initParams()
			newAnimal.position = newAnimalPosition
			self.power = self.power / 2
			result.append(Action(ActionEnum.A_ADD, newAnimalPosition, 0, newAnimal))
		return result

	def getNeighboringPosition(self):
		return self.world.getNeighboringPositions(self.position)

	def getNeighboringBirthPosition(self):
		return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))

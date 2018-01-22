class Bear(object):
	def sound(self):
		print "Groarrr"

class Dog(object):
	def sound(self):
		print "Woof Woof!"

def makeSound(animalType):
	animalType.sound()

bearobj = Bear()
dogobj = Dog()

makeSound(bearobj)
makeSound(dogobj)

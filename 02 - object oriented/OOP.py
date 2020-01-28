
class PlayerCharacter:
	# Class object
	member = True
	def __init__(self, name, age=0):
			self.name = name
			self.age = age

	def run(self):
			print('run')


player1 = PlayerCharacter('Bob', 60)
player1 = PlayerCharacter('Cindy', 20)


print(player1.name)



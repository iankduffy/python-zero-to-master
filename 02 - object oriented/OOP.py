
class PlayerCharacter:
	# Class object
	member = True
	def __init__(self, name, age=0):
			self.name = name
			self.age = age

	def run(self):
			print('run')
	
	@classmethod # can be called with out a player created
	def add_things(cls, num1, num2): 
		return num1 + num2

	@staticmethod
	def add_thing2(num1, num2):
		return num1 + num2


player1 = PlayerCharacter('Bob', 60)
player1 = PlayerCharacter('Cindy', 20)


print(player1.name)



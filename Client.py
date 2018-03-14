# coding=utf-8

class Client:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def __str__(self):
		return ("Name:{} Surname:{} \n".format(self.name, self.surname))

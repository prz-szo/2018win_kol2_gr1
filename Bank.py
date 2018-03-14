# coding=utf-8


class Bank:
	def __init__(self):
		self.list_of_clients = {}

	#def __str__(self):
		#return print("{} \n".format(self.list_of_clients))
	
	def add_client(self, client_to_add):
		self.list_of_clients[client_to_add] = 0

	def input(self, client_for_input, money):
		self.list_of_clients[client_for_input] += money

	def withdraw(self, client_for_input, money):
		clients_money = self.list_of_clients[client_for_input]
		if clients_money < money:
			print("No enough money on the account!")
		else:
			self.list_of_clients[client_for_input] -= money
	
	def get_info_about_client(self, client):
		return "{}\tMoney: {}".format(client, self.list_of_clients[client])

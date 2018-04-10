import os.path
import json


database = {}

def add_client(bank_name, client_name):
	global database
	if (not does_bank_exist(bank_name)):
		raise Exception("There is no such a bank!")
	elif (does_client_exist_in_bank(bank_name, client_name)):
		raise Exception("Provided client already exists in that bank!")
	else:
		database[bank_name][client_name] = 0

def add_bank(bank_name):
	global database
	if does_bank_exist(bank_name):
		raise Exception("Provided bank already exists!")
	else:
		database[bank_name] = {}

def deposit_money(bank_name, client_name, amount_of_money):
	if amount_of_money < 0:
		raise Exception("You cannot deposit negative amount of money!")
	elif not does_bank_exist(bank_name):
		raise Exception("There is no such a bank!")
	elif not does_client_exist_in_bank(bank_name, client_name):
		raise Exception("There is no such a client in {}!".format(bank_name))
	else:
		global database
		database[bank_name][client_name] += amount_of_money

def withdraw_money(bank_name, client_name, amount_of_money):
	global database
	if amount_of_money < 0:
		raise Exception("You cannot withdraw negative amount of money!")
	elif database[bank_name][client_name] < amount_of_money:
		raise Exception("You do not have such amount of money!")
	else:
		database[bank_name][client_name] -= amount_of_money

def transfer_money(sender_bank_name, sender_name, receiver_bank_name, receiver_name, amount_of_money):
	if amount_of_money < 0:
		raise Exception("You cannot deposit negative amount of money!")
	elif not does_bank_exist(sender_bank_name) or not does_bank_exist(receiver_bank_name):
		raise Exception("Both banks must exist!")
	elif not does_client_exist_in_bank(sender_bank_name, sender_name) \
		or not does_client_exist_in_bank(receiver_bank_name, receiver_name):
		raise Exception("Both clients must exist!")
	elif check_account_balance(sender_bank_name, sender_name) < amount_of_money:
		raise Exception("Sender do not have enough money!")
	else:
		deposit_money(receiver_bank_name, receiver_name, amount_of_money)
		withdraw_money(sender_bank_name, sender_name, amount_of_money)

def load_database_from_file(file_name):
	if (not os.path.isfile(file_name)):
		raise Exception("Provided file does not exist!")
	elif (file_name[-4:] != "json"):
		raise Exception("Provided file name must finish with '.json'!")
	else:
		with open(file_name, 'r') as file_to_read:
			global database
			database = json.load(file_to_read)
			print("\nDatabase has been loaded.\n")

def save_database_to_file(file_name):
	if (file_name[-4:] != "json"):
		raise Exception("Provided file name must finish with '.json'!")
	else:
		with open(file_name, 'w') as file_to_write:
			json.dump(database, file_to_write)
			print("\nDatabase has been saved.\n")

def check_account_balance(bank_name, client_name):
	return database[bank_name][client_name]

def does_bank_exist(bank_name):
	global database
	return bank_name in database

def does_client_exist_in_bank(bank_name, client_name):
	global database
	return client_name in database[bank_name]

if __name__ == '__main__':
	file_name = "bank_system.json"

	bank_1 = "SKOK"
	bank_2 = "Pocztowy"

	client_1 = "Zbigniew Kropka"
	client_2 = "Ignacy Stolkiewicz"

	add_bank(bank_1)
	add_bank(bank_2)

	add_client(bank_1, client_1)
	add_client(bank_2, client_2)

	deposit_money(bank_1, client_1, 100000)
	print("{} has {}$ in {} bank.".format(client_1, check_account_balance(bank_1, client_1), bank_1))

	save_database_to_file(file_name)
	database.clear()
	load_database_from_file(file_name)

	deposit_money(bank_2, client_2, 100)
	transfer_money(bank_1, client_1, bank_2, client_2, 10000)
	print("{} has {}$ in {} bank.".format(client_1, check_account_balance(bank_1, client_1), bank_1))
	print("{} has {}$ in {} bank.".format(client_2, check_account_balance(bank_2, client_2), bank_2))

	# # There is no client_2 in bank_1
	# withdraw_money(bank_1, client_2, 1234)

	# # There is no such a bank
	# withdraw_money(bank_2[-1], client_2, 1234)

	# # That file does not exist and also do not have .json ending
	# load_database_from_file(file_name[2:-2])

	# # You cannot withdraw such amount of money
	# withdraw_money(bank_2, client_2, -1)

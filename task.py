#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Good Luck

from Bank import Bank
from Client import Client

bank = Bank()
jan_kowalski = Client("Jan", "Kowalski")

bank.add_client(jan_kowalski)
bank.input(jan_kowalski, 1000)
print(bank.get_info_about_client(jan_kowalski))

bank.withdraw(jan_kowalski, 100)
print(bank.get_info_about_client(jan_kowalski))

bank.withdraw(jan_kowalski, 1000)
print(bank.get_info_about_client(jan_kowalski))

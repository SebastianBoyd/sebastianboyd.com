import time
import json
import datetime

def add_transaction(db):
	id = time.time()
        transaction = {}
        transaction['symbol'] = raw_input("Ender stock symbol: ")
	transaction['symbol'] = transaction['symbol'].upper()
        transaction['type'] = raw_input("Enter transaction type: ")
        date = raw_input("Enter date (mm/dd/yyyy) or now for the current time: ")
	if date == 'now':
		time_secs = time.time()
	else:
		date = date.split('/')
		date_tuple = datetime.date(int(date[2]), int(date[0]), int(date[1]))
        	date_tuple = date_tuple.timetuple()
		time_secs = time.mktime(date_tuple)
	transaction['time_secs'] = time_secs
	transaction['shares'] = input("Enter number of shares: ")
        transaction['price'] = input("Enter price per share: ")
	try:
        	transaction['commission'] = input("Enter commission: ")
        except:
		transaction['commission'] = 0
	transaction['notes'] = raw_input("Enter notes of transaction: ")
        if transaction['type'] == 'buy':
		db['cash'] = db['cash'] - transaction['price'] * transaction['shares']
		if transaction['symbol'] in db['owned_stocks']:
			db['owned_stocks'][transaction['symbol']] = db['owned_stocks'][transaction['symbol']] + transaction['shares']
		else:
			db['owned_stocks'][transaction['symbol']] = transaction['shares']
	elif transaction['type'] == 'sell':
		db['cash'] = db['cash'] + transaction['price'] * transaction['shares']
		if transaction['symbol'] in db['owned_stocks']:
                        db['owned_stocks'][transaction['symbol']] = db['owned_stocks'][transaction['symbol']] - transaction['shares']
                else:
                        db['owned_stocks'][transaction['symbol']] = transaction['shares'] * -1
	db['transaction'][id] = transaction
def deposit(db):
	amount = input("Enter amount to deposit: ")
	db['cash'] = db['cash'] + amount

def withdraw(db):
	amount = input("Enter amount to withdraw: ")
	db['cash'] = db['cash'] - amount

def enter_command():
	cmd = raw_input('Enter command: ')
	cmd.strip().lower()
	return cmd

def setup(db):
	db['cash'] = 0
	db['transaction'] = {}
	db['owned_stocks'] = {}

f = open("transactions.json", 'r')
string = f.read()
database = json.loads(string)
f.close()
while True:
	try:
		cmd = enter_command()
		if cmd == 'add':
			add_transaction(database)
		elif cmd == 'print':
			print database
		elif cmd == 'quit':
			break
		elif cmd == 'deposit':
			deposit(database)
		elif cmd == 'withdraw':
			withdraw(database)
		elif cmd == 'setup':
			setup(database)
			break
	finally:
		f = open("transactions.json", 'w')
		f.write(json.dumps(database, ensure_ascii=True))
		f.close()

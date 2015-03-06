import urllib2
import json
import time
def get_data(tickers):
	tickers = ','.join(map(str,tickers))
	response = urllib2.urlopen("http://www.google.com/finance/info?infotype=infoquoteall&q=" + tickers)
	string = response.read()
	string = string.strip('\n//')
	data = json.loads(string, object_hook=_decode_dict)
	return data

def update_chart(values):
	file = open('test.json', 'w')
	file.write(values)
	file.close()

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

def check_transactions():
	t = open('transactions.json', 'r')
	data = json.loads(t.read(), object_hook=_decode_dict)
	t.close()
	return data

def clean():
	values = "[null" + ", null" * 420 + "]"
	update_chart(values)

while True:
	now = time.localtime(time.time())
	minutes = (now[3] - 6) * 60 + now[4]
	print minutes
	if minutes < 0:
		clean()
	elif minutes < 421:
		file = open('test.json', 'r')
		old_chart = file.read()
		file.close()
		list_chart = json.loads(old_chart)
		transaction_data = check_transactions()
		data = get_data(transaction_data['owned_stocks'].keys())
		total_price = transaction_data['cash']
		for stocks in data:
			price = float(stocks['l'])
			shares = transaction_data['owned_stocks'][stocks['t']]
			total_price = total_price + price * shares
		
		print total_price
		file = open('current_price.json', 'w')
		file.write('[' + str(total_price) + ']')
		file.close()
		list_chart[minutes] = float(total_price)
		list_chart = str(list_chart)
		list_chart = list_chart.replace("None", 'null')
		update_chart(list_chart)
	time.sleep(60)

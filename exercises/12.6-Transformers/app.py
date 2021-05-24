incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

def my_var(object):
	return object['name'] +" "+ object['lastName']

transformed_data = list(map(my_var, incomingAJAXData ))
print(transformed_data)



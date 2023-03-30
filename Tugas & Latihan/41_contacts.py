
#json -> javascript object notation
fav_lang ={
	'Adri':'C',
	'Alfons':'Swift',
	'Chelvi':'Golang'
}

contacts = {
	'Jesse' : '0817335421',
	'Justin' : '089965785467',
	'Rayvin' : '081355936754'
}
print(f"Rayvin's number phone is {contacts['Rayvin']}")

#access value using get() / searching in dictionary

rayvin = contacts.get('Rayvin')
print(rayvin)
#dictionary = store data in to model a variety of real-world object


alien = {'color':'green', 'skill':'jumping'}#dict

player = {'username':'sukabapak', 'points':1000}
#accessing -> list index-value
#			  key-value
print(alien['color'])
print(player['points'])

#adding more information
#alien(100,200)
alien['x'] = 100
alien['y'] = 200

#modifiying
alien['color'] = 'tosca'

#delete
del player['points']
print(player)
print(alien)
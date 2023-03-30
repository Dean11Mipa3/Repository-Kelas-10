#Changing, Adding, Removing Element

motors = ['honda legenda', 'yamaha fizr', 'suzuki shogun']
print(motors)
#Changing / modifying
motors[1] = 'ducati'
print(motors)

#adding element
motors.append('kawasaki')
print(motors)

#inserting element
motors.insert(0, 'tvs')
print(motors)

motors.insert(2, 'viar')
print(motors)

#removing
motors.pop(2)
print(motors)

motors.remove('tvs')
print(motors)

del motors[0]
print(motors)
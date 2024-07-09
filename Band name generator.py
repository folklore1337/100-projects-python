import random


cities = ['Seoul ', 'Copenhagen ', 'Athens ', 'Milan ', 'Dortmund ']

pets = ['Dog', 'Cat', 'Mouse', 'Horse', 'Spider']

id = f'Ваш секретный код: ' + random.choice(cities) + random.choice(pets)
print(id)

# Example of using dictionaries with lists as values
# and accessing elements within them   
menus = { 'Breakfast': ['egg', 'spam', 'bacon'],
          'Lunch': ['jam', 'sausage', 'cheese'],
          'Dinner': ['grass', 'pastrami', 'tomato']}

print('Breakfast menu:' + str(menus['Breakfast']))
# Accessing individual items
print('First item on the breakfast menu: ' + menus['Breakfast'][0])
# Iterating through the dictionary
for name, menu in menus.items():
    print(name + ' menu: ' + str(menu))

person = {'name': 'Alice', 'age': 42, 'job': 'Engineer'}
print(person['name'] + ' is a ' + str(person['age']) + '-year old ' + person['job'] + '.')

# Alternative representation using lists of lists
menus =[ ['egg', 'spam', 'bacon'],
         ['jam', 'sausage', 'cheese'],
         ['grass', 'pastrami', 'tomato'] ]

print(menus[0][1])

# Dictionary to represent a person
person = {'name': 'Alice', 
          'age': 42, 
          'job': 'Engineer'}
print(person['name'] + ' is a ' + str(person['age']) + '-year old ' + person['job'] + '.')
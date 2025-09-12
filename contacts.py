# Example of using a dictionary with a list of dictionaries to store contacts
contacts = {
    'number': 4,
    'students':
        [
            {'name':'Alice Wonderland', 'email':'alice@cheshirecat.com'},
            {'name':'Jesus Jones', 'email':'jesus@godislove.com'},
            {'name':'Shaggy Doo', 'email':'wasted@mangled.com'},
            {'name':'Bob Holness', 'email':'bob@blockbusters.com'},
        ]
}
# Accessing elements in the list of dictionaries
print('Student emails:')
for student in contacts['students']:
    print(student['name'])
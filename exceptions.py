#print('hiya'))

acronyms = {'LOL': 'laughing out loud', 
            'WTF': 'what THE F'}

try:
    print(acronyms['WTF'])
    print(acronyms['OMG'])
except KeyError as e:
    print(f'KeyError: {e} does not exist in acronyms dictionary')
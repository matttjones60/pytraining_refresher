acronyms = {'LOL':'Laughing Out Loud',
           'ROFL':'Rolling On Floor Laughing',
           'LMAO':'Laughing My Ass Off'}

sentence = 'LMAO' + ' at my football team oh I just ' + 'LOL'
translation = acronyms.get('LOL') +' I just saw a pink buffalo '+acronyms.get('ROFL')

print(sentence)
print(translation)

definition = acronyms.get('BTW')

if definition:
    print(definition)
else:
    print("Key does not exist")
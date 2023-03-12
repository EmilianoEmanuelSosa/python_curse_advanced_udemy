
# Programa para comparar si dos palabras riman 


print('\n\n\n\nGive me two words and I will tell you if they rhyme\n\n\n\nsd')

firstword = input('tell me the first word')
secondword = input('tell me the second word')

if firstword[-3: ] == secondword[-3: ]:
    print('the words rhyme')
elif firstword [-2: ] == secondword[-2: ]:
    print('the words rhyme a little')
elif len(firstword) < 2 or len(secondword) < 2:
    print('word very short, please review.')
else:
    print('the words dont rhyme')


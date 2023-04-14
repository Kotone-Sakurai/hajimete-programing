import random

verbs = ['run', 'find', 'put away']
adjectives = ['beautiful', 'nice', 'terrible']
nouns = ['dog', 'cat', 'shota']

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = 'I ' + verb + ' ' + adjective + ' ' + noun + '.'

print(phrase)
 

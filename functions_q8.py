# q.8 Use Python's control structures to create a function that takes an ISO 639-1 language 
# code and returns a greeting in that language. You can take the examples below or add 
# whatever languages you like.
def greet(language):
    match language:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt': 
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'Code not found in file.'

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print(greet('fd'))
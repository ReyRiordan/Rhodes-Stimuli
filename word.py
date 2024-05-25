import random


def generate_basic() -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Generating a random length for the noun (between 3 and 8 characters)
    length = random.randint(3, 8)
    
    # Generating random characters for the noun
    noun = ''
    for i in range(length):
        if i % 2 == 0:
            noun += random.choice(consonants)
        else:
            noun += random.choice(vowels)
    
    return noun
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


def generate_harmonic() -> list[str]:
    vowels = 'eiou'
    consonants = 'pbtdgknmsz'
    root_dict = {'front': 'ei', 'back': 'ou'}
    suffix_dict = {'front': 'i', 'back': 'u'}

    type = random.choice(['front', 'back'])

    c1 = random.choice(consonants)
    v1 = random.choice(root_dict[type])
    c2 = random.choice(consonants)
    v2 = random.choice(root_dict[type])
    root = c1 + v1 + c2 + v2

    plural = root + 'm' + suffix_dict[type]

    violation = root + 'm' + suffix_dict['back'] if type == 'front' else root + 'm' + suffix_dict['front']

    return [root, plural, violation]


def generate_firstlast() -> list[str]:
    vowels = 'eiou'
    consonants = 'pbtdgknmsz'
    root_dict = {'front': 'ei', 'back': 'ou'}
    suffix_dict = {'front': 'i', 'back': 'u'}

    type = random.choice(['front', 'back'])

    c1 = random.choice(consonants)
    v1 = random.choice(root_dict[type])
    c2 = random.choice(consonants)
    v2 = random.choice(root_dict['back']) if type == 'front' else random.choice(root_dict['front'])
    root = c1 + v1 + c2 + v2

    plural = root + 'm' + suffix_dict[type]

    violation = root + 'm' + suffix_dict['back'] if type == 'front' else root + 'm' + suffix_dict['front']

    return [root, plural, violation]

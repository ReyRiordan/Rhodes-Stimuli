
vowels = 'eiou'
consonants = 'pbtdgknmsz'
root_dict = {'front': 'ei', 'back': 'ou'}
suffix_dict = {'front': 'i', 'back': 'u'}

with open('stimuli/firstlast_violations.txt', 'w') as file:
    for type in ['front', 'back']:
        for c1 in consonants:
            for v1 in root_dict[type]:
                for c2 in consonants:
                    for v2 in (root_dict['back'] if type == 'front' else root_dict['front']):
                        root = c1 + v1 + c2 + v2
                        violation = root + 'm' + suffix_dict['back'] if type == 'front' else root + 'm' + suffix_dict['front']
                        file.write(f"{violation}\n")
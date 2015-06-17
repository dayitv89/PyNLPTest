#! /usr/bin/python
findAll = {}
def init():
    ALL = {
    'I' : ['I', 'me', 'mine', 'main', 'mera', 'maine'],
    'YOU' : ['you', 'your', 'tum', 'tumhara', 'aap', 'aapka', 'tu', 'tera' ],
    'HE' : ['he', 'his', 'him', 'wo', 'vah', 'wah'],
    'WHAT' : ['what', 'kya'],
    'IS' : ['is', 'hai'],
    'AM' : ['hai'],
    'WAS' : ['was', 'tha']
    }
    for key, value in ALL.items():
        for x in value:
            x = x.upper()
            if x in findAll:
                findAll[x] = findAll[x] + [key]
            else:
                findAll[x] = [key]
init()

def parse(sentance):
    print [meaningWord(a) for a in sentance.split()]

def meaningWord(word):
    if word.upper() in findAll:
        return findAll[word.upper()]
    return '#' + word

parse('kya hai tera naam')

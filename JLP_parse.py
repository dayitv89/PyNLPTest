from JLP import JLP

def parse(sentance):
    findAll = JLP().getFindAll()
    return [meaningInLib(a, findAll) for a in sentance.split()]

def meaningInLib(word, findAll):
    if word.upper() in findAll:
        return findAll[word.upper()]
    return ['#' + word]

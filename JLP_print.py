from JLP import JLP

def start_print(ALL):
    jlp = JLP()
    findAll = jlp.getFindAll()
    CMDs = jlp.getCMDs()
    stmt_parse = ALL.split()
    if len(stmt_parse) < 2:
        print '\n-------------------------------------\n'
    elif stmt_parse[1] in findAll or stmt_parse[1].upper() in findAll:
        print findAll[stmt_parse[1].upper()]
    elif stmt_parse[1] in CMDs or stmt_parse[1].lower() in CMDs:
        print CMDs[stmt_parse[1].lower()] + ": CMD Found"
    else:
        print '#Error: LANG/CMD not available'

from JLP_parse import *
from JLP import JLP

findAll = JLP().getFindAll()
def callingAMethod(method_name, args):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
         raise Exception("Method %s not implemented" % method_name)
    method(args)

def start_add_lang(stmts):
    ALL = {stmts[2].upper() : stmts[3:]}
    for key, value in ALL.items():
        for x in value:
            x = x.upper()
            if x in findAll:
                if key not in findAll:
                    findAll[x] = findAll[x] + [key]
            else:
                findAll[x] = [key]
    JLP().setFindAll(findAll)
    print '#SUCCESS: Lang added successfully :'+ str(ALL)

def start_add(ALL):
    findAll = JLP().getFindAll()
    stmt_parse = ALL.split()
    add_parse = {'lang':4, 'cmd':2}
    if stmt_parse[1] in add_parse:
        if len(stmt_parse) < add_parse[stmt_parse[1]]:
            print '#ERROR: CMD argu length'
            return
        callingAMethod('start_'+stmt_parse[0]+'_'+stmt_parse[1], (stmt_parse))
    else:
        print '#ERROR: CMD argu not found'

    # for key, value in ALL.items():
    #     for x in value:
    #         x = x.upper()
    #         if x in findAll:
    #             findAll[x] = findAll[x] + [key]
    #         else:
    #             findAll[x] = [key]
    # f = open("lang_Hn","w")
    # f.write(json.dumps(findAll))
    # f.close()

def start_rm(ALL):
    findAll = JLP().getFindAll()
    stmt_parse = ALL.split()
    add_parse = {'lang':3, 'cmd':2}
    if stmt_parse[1] in add_parse:
        if len(stmt_parse) < add_parse[stmt_parse[1]]:
            print '#ERROR: CMD argu length'
            return
        callingAMethod('start_'+stmt_parse[0]+'_'+stmt_parse[1], (stmt_parse))
    else:
        print '#ERROR: CMD argu not found'

def start_rm_lang(stmts):
    rm = stmts[2].upper()
    if rm not in findAll:
        print '#ERROR: key not found: ' + rm
        return

    if len(stmts) > 3:
        if stmts[3].upper() == 'ALL' or stmts[3].upper() == '#ALL':
            del findAll[rm]
            print '#SUCCESS: removed :'+rm
            return

    print findAll[rm]
    keys = raw_input("Enter keys to remove / #all $ ")
    keys = keys.split()
    if len(keys) == 0:
        print '#ERROR: no input found'
    elif len(keys) == 1 and keys[0].upper() == '#ALL':
        del findAll[rm]
    else:
        rm_valueArray = findAll[rm]
        for key in keys:
            if key.upper() in rm_valueArray:
                rm_valueArray = rm_valueArray.remove(key.upper())
                print "#SUCCESS: removed :"+key
            else:
                print "#ERROR: key not found"+ key
        if len(findAll[rm]) == 0:
            del findAll[rm]
        else:
            findAll[rm] = rm_valueArray

    JLP().setFindAll(findAll)

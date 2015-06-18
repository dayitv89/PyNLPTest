class Global(object):
    def callingAMethod(self ,method_name, args):
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(method_name)
        if not method:
             raise Exception("Method %s not implemented" % method_name)
        method(args)

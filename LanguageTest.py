#! /usr/bin/python

from JLP import JLP
jlp = JLP()

CMDs = jlp.getCMDs()

from JLP_add import start_add, start_rm
from JLP_parse import parse
from JLP_print import start_print

def callingAMethod(method_name, args):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
         raise Exception("Method %s not implemented" % method_name)
    method(args)

def cmdMode():
    while True:
        ip = raw_input("\nJamesLP$ ")
        cmd = ip.split()
        if len(cmd) == 0:
            continue
        if cmd[0] in CMDs:
            callingAMethod('start_'+cmd[0], ip)
        else:
            print parse(ip)

def start_exit(self):
    exit()

cmdMode()

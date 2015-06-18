import json

class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]

class JLP(Singleton):
    findAll = {}
    CMDs = []
    def __init__(self):
        f1 = open("lang_Hn",'r')
        self.findAll = json.loads(f1.read())
        f2 = open("lang_CMDs",'r')
        self.CMDs = json.loads(f2.read())

    def setFindAll(self, newFindAll):
        self.findAll = newFindAll
        f = open("lang_Hn","w")
        f.write(json.dumps(newFindAll))
        f.close()

    def getFindAll(self):
        return self.findAll

    def setCMDs(self, newCMDs):
        self.CMDs = newCMDs
        f = open("lang_CMDs","w")
        f.write(json.dumps(newCMDs))
        f.close()

    def getCMDs(self):
        return self.CMDs


from sc2common.commonUtilFuncs import standardizeMapName
import re


################################################################################
class MapRecord(object):
    ############################################################################
    def __init__(self, name, path, attrs):
        self.name = standardizeMapName(name)
        self.path = path
        for a in attrs:
            a = a.lower()
            val = re.search("^([a-z]+)([\d_]\w*)$", a)
            if val:
                a,val = val.groups()
                try:    val = int(val)
                except: val = val.lstrip('_')
            else:
                val = True
            setattr(self, a, val)
    ############################################################################
    def __str__(self):  return self.__repr__()
    def __repr__(self): return "<%s \"%s\">"%(self.__class__.__name__, self.name)
    ############################################################################
    @property
    def attrs(self):
        try:    return self._attrs
        except AttributeError: pass
        self._attrs = [a for a in self.__dict__ if a not in ["name", "path"]]
        return self._attrs
    ############################################################################
    def display(self):
        print(self)
        for a in self.attrs:
            print("    %6s : %s"%(a, self.__dict__[a]))


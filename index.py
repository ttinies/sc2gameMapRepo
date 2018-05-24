
from glob import glob
import os

from sc2scenarios.mapRecord import MapRecord
from sc2common import constants as c
from sc2scenarios import defs as d

################################################################################
class IndexCache(object):
    def __init__(self): pass
cache = IndexCache()


################################################################################
def getIndex(folderPath=d.MAPS_FOLDER):
    try:    return cache.structure
    except AttributeError: pass # if it doesn't exist, generate and cache the map file data
    ############################################################################
    def folderSearch(path, attrList=[]):
        ret = []
        for item in glob(os.path.join(path, '*')):
            if item == os.sep: continue
            itemName = os.path.basename(item)
            if   os.path.isdir(item):               ret += folderSearch(item, attrList + [itemName])
            elif itemName.endswith(c.SC2_FILE_MAP): ret.append( MapRecord(itemName, item, attrList) )
        return ret
    ############################################################################    
    cache.structure = folderSearch(folderPath)
    return cache.structure


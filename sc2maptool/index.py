
from glob import glob
import os

from sc2gameMapRepo.mapRecord import MapRecord
from sc2gameMapRepo import constants as c

################################################################################
class IndexCache(object):
    def __init__(self): pass
cache = IndexCache()


################################################################################
def getIndex(folderPath=c.MAPS_FOLDER):
    """parse the 'Maps' subfolder directory divining criteria for valid maps"""
    try:    return cache.structure
    except AttributeError: pass # if it doesn't exist, generate and cache the map file data
    ############################################################################
    def folderSearch(path, attrList=[]):
        ret = []
        for item in glob(os.path.join(path, '*')):
            if item == os.sep: continue
            itemName = os.path.basename(item)
            if   os.path.isdir(item):               ret += folderSearch(item, attrList + [itemName])
            elif itemName.endswith(c.SC2_MAP_EXT):  ret.append( MapRecord(itemName, item, attrList) )
        return ret
    ############################################################################    
    cache.structure = folderSearch(folderPath)
    return cache.structure


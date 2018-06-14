from sc2maptool import selectMap
from sc2maptool.mapRecord import MapRecord

def simple_test():
    for m in selectMap(name="flat", melee=True, excludeName=True, closestMatch=False):
        assert isinstance(m, MapRecord)

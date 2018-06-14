from sc2maptool import selectMap
from sc2maptool.mapRecord import MapRecord

def test_simple():
    for m in selectMap(name="flat", melee=True, excludeName=True, closestMatch=False):
        assert isinstance(m, MapRecord)

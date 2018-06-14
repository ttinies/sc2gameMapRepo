
import os


MAPS_FOLDER     = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Maps")
SC2_MAP_EXT     = "SC2Map"

EXCLUDED_KEYS   = ["mapname", "exclude", "best", "details", "list", "path"]

class InvalidMapSelection(Exception): pass


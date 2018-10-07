
import distutils.dir_util
import os
import shutil

from sc2gameLobby import config

from sc2maptool.__version__ import __version__
from sc2maptool import constants as c


################################################################################
def setup():
    """ensure that the maptool's maps are installed in the SC2 install maps """\
    """directory simply by importing this module"""
    try:
        _cfg = config()
        maptoolDir = os.path.join(_cfg.installedApp.mapsDir, c.PATH_MAPTOOLDIR)
    except Exception as e: # allow installation on machines without Starcraft 2 installed (i.e. travis cloud testing machines)
        print("WARNING: %s"%e)
        maptoolDir = c.MAPS_FOLDER # default to the package's map library
    c.PATH_MAP_INSTALL = os.path.join(maptoolDir, __version__)
    if not os.path.isdir(c.PATH_MAP_INSTALL):
        if os.path.isdir(maptoolDir):  shutil.rmtree(maptoolDir) # clean up previous installations (avoid endlessly growing map repository)
        distutils.dir_util.copy_tree(c.MAPS_FOLDER, c.PATH_MAP_INSTALL) # make the directories, always ensuring all parents are created appropriately (also handling potential race conditions)
    return c.PATH_MAP_INSTALL


################################################################################
if __name__ == "__main__":  setup()


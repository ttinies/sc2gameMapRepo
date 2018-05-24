
from __future__ import absolute_import
from __future__ import division       # python 2/3 compatibility
from __future__ import print_function # python 2/3 compatibility

from sc2scenarios import selectMap, getIndex
import sys


#################################################################################
if __name__=='__main__': # mini/unit test
    """
    PURPOSE: command-line interface for map information
    """
    from argparse import ArgumentParser
    usage_def = ""#usage:  %prog  <gameVersion>  <options>"
    parser = ArgumentParser(usage_def)
    #parser.add_argument("-v", "--verbosity", type=int, default=vLvl, help="The desired verbosity level to reflect in stdout printing")
    #parser.add_argument("-s", "--save", action="store_true", help="Force the data to be saved.")
    parser.add_argument("--list"       , default=None, action="store_true", help="Display all known maps by category.")
    parser.add_argument("--mapname"                                       , help="the name of the specific map to load.")
    parser.add_argument("--ladder"     , default=None, type=bool          , help="whether ladder must be selected (True) or ignored")
    parser.add_argument("--combat"     , default=None, type=bool          , help="whether combat maps must be selected (True) or ignored")
    parser.add_argument("--economy"    , default=None, type=bool          , help="whether economy maps must be seleced (True) or ignored")
    parser.add_argument("--misc"       , default=None, type=bool          , help="whether misc maps must be seleced (True) or ignored")
    parser.add_argument("--test"       , default=None, type=bool          , help="whether test maps must be seleced (True) or ignored")
    parser.add_argument("--year"       , default=None, type=int           , help="the calendar year the ladder season occurred.")
    parser.add_argument("--season"     , default=None, type=int, 
                                                       choices=[1, 2, 3, 4],help="the specific ladder season within a calendar year.")
    parser.add_argument("--mode"       , default=None, choices=["1v1", "2v2", "3v3", "4v4"],
                                                                            help="the official ladder category to play.")
    #parser.add_argument('entities', nargs='*') # the remaining arguments are processed together
    options = parser.parse_args()
    #sys.argv = sys.argv[:1] # remove all arguments to avoid problems with absl FLAGS :(
    if options.list:
        for v in getIndex():
            v.display()
        sys.exit(0)
    params = {k:v for k,v in options._get_kwargs() if v!=None and k not in ["mapname", "path"]}
    selectMap(options.mapname, **params).display()


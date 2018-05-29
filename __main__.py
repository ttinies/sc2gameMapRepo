
from __future__ import absolute_import
from __future__ import division       # python 2/3 compatibility
from __future__ import print_function # python 2/3 compatibility

from sc2gameMapRepo import constants as c
from sc2gameMapRepo.functions import selectMap, filterMapAttrs, filterMapNames
from sc2gameMapRepo.index import getIndex


#################################################################################
if __name__=='__main__': # mini/unit test
    """
    PURPOSE: command-line interface for map information
    """
    from argparse import ArgumentParser
    usage_def = ""#usage:  %prog  <gameVersion>  <options>"
    parser = ArgumentParser(usage_def)
    # main routine behavior
    parser.add_argument("--list"       , default=None, action="store_true", help="Display all known maps by category.")
    parser.add_argument("--details"    , default=None, action="store_true", help="show details of each mapname.")
    parser.add_argument("--path"       , default=None, action="store_true", help="provide the absolute path to the file")
    # function operation parameters
    parser.add_argument("--mapname"    , default=""                       , help="the name of the specific map to load.")
    parser.add_argument("--exclude"    ,               action="store_true", help="exclude maps with names specified by --mapname.")
    parser.add_argument("--best"       ,               action="store_true", help="match maps that are closer with --mapname")    
    # record match criteria
    parser.add_argument("--ladder"     , default=None, type=bool          , help="ladder must be selected (True) or ignored.")
    parser.add_argument("--combat"     , default=None, type=bool          , help="combat maps must be selected (True) or ignored.")
    parser.add_argument("--economy"    , default=None, type=bool          , help="economy maps must be selected (True) or ignored.")
    parser.add_argument("--scenario"   , default=None, type=bool          , help="single-player games with a specific objective to achieve must be selected (True) or ignored.")
    parser.add_argument("--misc"       , default=None, type=bool          , help="misc maps must be seleced (True) or ignored.")
    parser.add_argument("--test"       , default=None, type=bool          , help="test maps must be seleced (True) or ignored.")
    parser.add_argument("--year"       , default=None, type=int           , help="the calendar year the ladder season occurred.")
    parser.add_argument("--season"     , default=None, type=int, 
                                                       choices=[1, 2, 3, 4],help="the specific ladder season within a calendar year.")
    parser.add_argument("--mode"       , default=None, choices=["1v1", "2v2", "3v3", "4v4"],
                                                                            help="the official ladder category to play.")
    options = parser.parse_args()
    params = {k:v for k,v in options._get_kwargs()\
        if v!=None and k not in c.EXCLUDED_KEYS}
    if options.list or options.details:
        specifiedMaps = filterMapNames(
            options.mapname,
            records = filterMapAttrs(**params),
            excludeRegex=options.exclude,
            closestMatch=options.best
        )
        if specifiedMaps:
            for v in specifiedMaps:
                if options.details: v.display()
                else:               print(v)
            print("Found %d maps that match given criteria."%(len(specifiedMaps)))
        else:
            print("No matching maps found.")
    else:
        specifiedMaps = selectMap(
            options.mapname,
            excludeName =options.exclude,
            closestMatch=options.best,
            **params)
        if not isinstance(specifiedMaps, list):
            specifiedMaps = [specifiedMaps]
        for m in specifiedMaps:
            if options.path:    print(m.path)
            else:               print(m.name)


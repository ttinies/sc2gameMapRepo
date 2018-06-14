
from six import iteritems # python 2/3 compatibility

import random
import re

from sc2maptool.index import getIndex
from sc2maptool import constants as c


################################################################################
def selectMap(name=None, excludeName=False, closestMatch=True, **tags):
    """select a map by name and/or critiera"""
    matches = filterMapAttrs(**tags)
    if not matches: raise c.InvalidMapSelection("could not find any matching maps given criteria: %s"%tags)
    if name: # if name is specified, consider only the best-matching names only
        matches = filterMapNames(name, excludeRegex=excludeName, closestMatch=closestMatch, records=matches)
    try:
        if closestMatch:    return random.choice(matches) # pick any map at random that matches all criteria
        elif matches:       return matches
    except IndexError: pass # matches is empty still
    raise c.InvalidMapSelection("requested map '%s', but could not locate "\
        "it within %s or its subdirectories."%(name, c.MAPS_FOLDER))


################################################################################
def filterMapAttrs(records=getIndex(), **tags):
    """matches available maps if their attributes match as specified"""
    if len(tags) == 0: return records # otherwise if unspecified, all given records match
    ret = []
    for record in records: # attempt to match attributes
        if matchRecordAttrs(record, tags):
            ret.append(record)
    return ret


################################################################################
def matchRecordAttrs(mapobj, attrs):
    """attempt to match given attributes against a single map object's attributes"""
    for k,v in iteritems(attrs):
        try:    val = getattr(mapobj, k)
        except AttributeError:       # k isn't an attr of record
            if v:       return False # if k doesn't exist in mapobj but was required, no match
            else:       continue     # otherwise ignore attributes that aren't defined for the given map record
        if val != v:    return False # if any criteria matches, it's considered a match
    return True                      # all criteria matched at all


################################################################################
def filterMapNames(regexText,  records=getIndex(), excludeRegex=False, closestMatch=True):
    """matches each record against regexText according to parameters
    NOTE: the code could be written more simply, but this is loop-optimized to
          scale better with a large number of map records"""
    bestScr = 99999 # a big enough number to not be a valid file system path
    regex = re.compile(regexText, flags=re.IGNORECASE)
    ret = []
    if excludeRegex: # match only records that do NOT contain regex
        if regexText and closestMatch: # then maps with fewer characters are better matches
            for m in list(records):
                if re.search(regex, m.name): continue # map must NOT contain specified phrase
                score = len(m.name) # the map with the smallest map name means it has the largets matching character percentage
                if score == bestScr:
                    bestScr = score
                    ret.append(m)
                elif score <  bestScr: # new set of best maps
                    bestScr = score
                    ret = [m]
        else: # all maps that match regex are included
            for m in list(records):
                if re.search(regex, m.name): continue # map must NOT contain specified phrase
                ret.append(m) # any mapname containing regex matches
    else: # only match records that contain regex
        if regexText and closestMatch: # then maps with fewer characters are better matches
            for m in records:
                if not re.search(regex, m.name): continue # map must contain specified phrase if excludeRegex==True
                score = len(m.name) # the map with the smallest map name means it has the largets matching character percentage
                if score == bestScr:
                    bestScr = score
                    ret.append(m)
                elif score <  bestScr: # new group of best maps
                    bestScr = score
                    ret = [m]
        else: # all maps that match regex are included
            for m in records:
                if not re.search(regex, m.name): continue # map must contain specified phrase if excludeRegex==True
                ret.append(m) # any mapname containing regex matches
    return ret



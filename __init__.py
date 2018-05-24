"""
Copyright 2018 Versentiedge LLC All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS-IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import absolute_import
from __future__ import division       # python 2/3 compatibility
from __future__ import print_function # python 2/3 compatibility

from six import iteritems # python 2/3 compatibility

import random
import re

from .index import getIndex
from . import defs

from sc2common import constants as c


################################################################################
def selectMap(name=None, **args):
    allMaps = getIndex()
    matches = []
    ############################################################################
    def matchRecordAttrs(mapobj, attrs):
        """attempt to match attributes"""
        for k,v in iteritems(attrs):
            try:    val = getattr(record, k)
            except AttributeError:       # k isn't an attr of record
                if not v:   return True  # if k doesn't exist in mapobj but was required, no match
                else:       continue     # otherwise ignore attributes that aren't defined for the given map record
            if val == v:    return True  # if any criteria matches, it's considered a match
        return False                     # no criteria matched at all
    ############################################################################
    for record in allMaps: # attempt to match attributes
        if not args or matchRecordAttrs(record, args):
            matches.append(record)
    if not matches: raise c.InvalidMapSelection("could not find any matching maps given criteria: %s"%args)
    if name: # if name is specified, consider only the best-matching names only
        bestScr = 99999 # a big enough number to not be a valid file system path
        regex = re.compile("^%s"%name, flags=re.IGNORECASE)
        for m in list(matches):
            if not re.search(regex, m.name): # map must contain specified phrase
                matches.remove(m)
                continue
            score = len(m.name) # the map with the smallest map name means it has the largets matching character percentage
            if score <= bestScr:    bestScr = score
            else:                   matches.remove(m)
    try:    return random.choice(matches) # pick any map at random that matches all criteria
    except IndexError: # matches is empty still
        raise c.InvalidMapSelection("requested map '%s', but could not locate "\
            "it within %s or its subdirectories."%(name, defs.MAPS_FOLDER))


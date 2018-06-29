from sc2maptool import cli
from sc2maptool import functions as f
from sc2maptool import index
from sc2maptool import selectMap
from sc2maptool import standardizeMapName
from sc2maptool.mapRecord import MapRecord


def test_cli():
    import sys
    sys.argv = ['', "--mapname=MechDepot", "--list", "--season=3"]
    cli()
    sys.argv = ['', "--mapname=MechDepot", "--details"]
    cli()
    sys.argv = ['', "--mapname=zx", "--details"]
    cli()
    sys.argv = ['', "--mapname=zx"]
    cli()
    sys.argv = ['', "--mapname=a", "--best"]
    cli()
    sys.argv = ['', "--mapname=zz", "--list"]
    cli()
    sys.argv = ['', "--mapname=a", "--best", "--path"]
    cli()
    from sc2maptool import __main__


def test_index():
    idx1 = index.getIndex()
    idx2 = index.getIndex()
    newCache = index.IndexCache()
    assert len(index.c.EXCLUDED_KEYS) == 6
    x = index.c.InvalidMapSelection()
    try:
        raise index.c.InvalidMapSelection("test")
        assert False
    except:
        assert True
    assert isinstance(index.c.MAPS_FOLDER, str)
    assert isinstance(index.c.SC2_MAP_EXT, str)


def test_simple():
    for m in selectMap(name="flat", melee=True, excludeName=True, closestMatch=False):
        assert isinstance(m, MapRecord)
        assert isinstance(m.rawData, bytes) # requires real paths


def test_filter_map():
    r1 = f.filterMapAttrs(ladder=False)
    r2 = f.filterMapAttrs(r1) # no tags means return param as is
    assert r1 == r2


def test_match_attrs():
    boardwalk = selectMap("boardwalk")
    assert False == f.matchRecordAttrs(boardwalk, {"asdjfd":True})
    assert True  == f.matchRecordAttrs(boardwalk, {"asdjfd":None})
    assert True  == f.matchRecordAttrs(boardwalk, {"asdjfd":""})
    assert True  == f.matchRecordAttrs(boardwalk, {"asdjfd":0})
    assert True  == f.matchRecordAttrs(boardwalk, {"asdjfd":False})
    assert False == f.matchRecordAttrs(boardwalk, {"year":2016})
    assert True  == f.matchRecordAttrs(boardwalk, {"year":2017})
    assert True  == f.matchRecordAttrs(boardwalk, {})


def test_filter_map_names():
    r = f.filterMapNames("nav", closestMatch=False)
    assert len(r) == 1
    assert r[0].name == "MoveToBeaconAvoidBaneling"
    r = f.filterMapNames("w[ea][rt]", closestMatch=False)
    rNames = {m.name for m in r}
    display_test(rNames, len(rNames), 3)
    assert "Backwater"          in rNames
    assert "Eastwatch"          in rNames
    assert "FlowerFields"       in rNames
    rNames = {m.name for m in f.filterMapNames("at", closestMatch=True)}
    display_test(rNames, len(rNames), 4)
    assert "Flat32"             in rNames
    assert "Flat48"             in rNames
    assert "Flat64"             in rNames
    assert "Flat96"             in rNames
    rNames = {m.name for m in f.filterMapNames("[rst]e", closestMatch=True)}
    display_test(rNames, len(rNames), 3)
    assert "Acolyte"            in rNames
    assert "Odyssey"            in rNames
    assert "RedCity"            in rNames
    rNames = {m.name for m in f.filterMapNames("bi", closestMatch=True)}
    display_test(rNames, len(rNames), 1)
    assert "16Bit"              in rNames
    rNames = {m.name for m in f.filterMapNames("[amoqy6]", excludeRegex=True, closestMatch=False)}
    display_test(rNames, len(rNames), 3)
    assert "Redshift"           in rNames
    assert "BelShirVestige"     in rNames
    assert "NewkirkPrecinct"    in rNames
    rNames = {m.name for m in f.filterMapNames("[ej]", excludeRegex=True, closestMatch=True)}
    display_test(rNames, len(rNames), 2)
    assert "16Bit"              in rNames
    assert "Frost"              in rNames


def test_map_record():
    x = MapRecord("test", "testpath", ["ftrue", "fval123bc", "fint12"])
    assert x.display() == None
    assert type(str(x)) == str
    assert type(repr(x)) == str
    assert x.ftrue == True
    assert x.fval  == "123bc"
    assert x.fint  == 12
    assert len(x.attrs) == 4


def test_map_selection():
    """verify the functionality of selectMap()"""
    for i in range(100): # without any params, a single map should always selected
        assert isinstance(selectMap(), MapRecord)
    casesInclusion = [
        # INPUT TEST CASE   EXPECTED RESULT
        ("zerg",            ["DefeatZerglingsAndBanelings", "FindAndDefeatZerglings"]),
        ("AndBane",         ["DefeatZerglingsAndBanelings"]),
        ("e[ar].*r$",       ["Interloper", "Dreamcatcher"]), #accepts regular expression
        ("^b.*a.*k$",       ["BattleOnTheBoardwalk", "Blackpink", "Blackpink"]),
        ("x",               ["ProximaStation", "ProximaStation", "TraitorsExile", "TraitorsExile"]), # identifies multiple results for their unique paths
        ("^x",              Exception), # none of the maps start with an 'x'
        ("^abi",            ["Abiogenesis"]),
        ("128$",            ["Flat128", "Simple128"]),
        (".{1}[^o]nt",      ["AcidPlant", "AcidPlant", "LastRemnant", "LastRemnant"]),
    ]
    casesExclusion = [
        # INPUT TEST CASE   EXPECTED RESULT
        ("[\w]",            Exception), # if ignoring all valid chars, error!
        ("[aeiou]",         Exception), # all maps have a vowel
        ("[aiy]",           ["Honorgrounds", "Sequencer", "Frost", "MechDepot", "Redstorm"]), # all maps without an a, i or y
        ("[cefgjk1xz]",       ["BloodBoil", "HitAndRun", "MistySwamp"]),
        ("^[^p]",           ["PaladinoTerminal", "ProximaStation", "ProximaStation", "PredictBattleOutcome", "PrimevalWilds", "PrimevalWilds"]),
        ("[aiot]",          ["Sequencer"]),
    ]
    def iterCases(cases, exclusion):
        for thisInput, thisExpect in cases:
            try:    mapResults = selectMap(name=thisInput, excludeName=exclusion, closestMatch=False)
            except:
                display_test(thisInput, Exception, thisExpect)
                continue
            print(">>", mapResults)
            for m in mapResults:
                display_test("%s in %s"%(m.name, thisExpect), m.name in thisExpect, True)
            display_test(thisInput, len(mapResults), len(thisExpect))
    iterCases(casesInclusion, False)
    iterCases(casesExclusion, True)
    newMap = selectMap(year=2018, season=1) # get exactly one map
    assert not isinstance(newMap, list)
    try:    assert selectMap(year=1970) and False
    except: assert True # bad attrs causes an exception
    try:    assert selectMap("z", mode="1v1", year=2018, season=2) and False
    except: assert True # force attribute selection AND bad name filtering resuling in no matches
    try:    assert selectMap("[\w]", excludeName="ujari", closestMatch=True, ladder=True) and False
    except: assert True


def test_names():
    """verify the functionality of standardizeMapName()"""
    cases = [
        # INPUT TEST CASE               EXPECTED RESULT          WHAT IS TESTED
        (None,                          Exception           ), # bad input
        ("abcd/12",                     "12"                ), # ignores path
        ("ksNmsQpLMdiMs",               "ksNmsQpLMdiMs"     ), # maintains case
        ("test123.SC2Map",              "test123"           ), # ignores extension
        ("AbiogenesisLE.SC2Map",        "Abiogenesis"       ), # ignores name descriptors
        ("/2017/s3/AcolyteLE.SC2Map",   "Acolyte"           ), # tests everything
    ]
    for thisInput, thisExpect in cases:
        try:    thisResult = standardizeMapName(thisInput)
        except: thisResult = Exception
        display_test(thisInput, thisResult, thisExpect)


def display_test(testIn, testOut, testExpect):
    """display test condition and its result, then assert the result"""
    print("%s%s =>  %s == %s"%(testIn, " "*max(0, 30-len(str(testIn))), testOut, testExpect))
    assert testExpect == testOut


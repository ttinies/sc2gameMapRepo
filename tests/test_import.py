from sc2maptool import selectMap
from sc2maptool import standardizeMapName
from sc2maptool.mapRecord import MapRecord

def test_simple():
    for m in selectMap(name="flat", melee=True, excludeName=True, closestMatch=False):
        assert isinstance(m, MapRecord)
        assert isinstance(m.rawData, bytes) # requires real paths


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
        ("x",               ["ProximaStation", "ProximaStation"]), # identifies multiple results for their unique paths
        ("^x",              Exception), # none of the maps start with an 'x'
        ("^abi",            ["Abiogenesis"]),
        ("128$",            ["Flat128", "Simple128"]),
        (".{1}[^o]nt",      ["AcidPlant", "AcidPlant"]),
    ]
    casesExclusion = [
        # INPUT TEST CASE   EXPECTED RESULT
        ("[\w]",            Exception), # if ignoring all valid chars, error!
        ("[aeiou]",         Exception), # all maps have a vowel
        ("[aiy]",           ["Honorgrounds", "Sequencer", "Frost", "MechDepot"]), # all maps without an a, i or y
        ("[cefgxk1]",       ["BloodBoil", "HitAndRun"]),
        ("^[^p]",           ["PaladinoTerminal", "ProximaStation", "ProximaStation", "PredictBattleOutcome"]),
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


if __name__=="__main__":
    #test_simple()
    test_map_record()
    #test_names()
    #test_map_selection()



import os


MAPS_FOLDER     = os.path.join(os.path.dirname(os.path.abspath(__file__)), "maps")
SC2_MAP_EXT     = "SC2Map"

EXCLUDED_KEYS   = ["mapname", "exclude", "best", "details", "list", "path"]

class InvalidMapSelection(Exception): pass

_16BIT              = "16bit"
ACID_PLANT          = "AcidPlant"
BATTLE_ON_BOARDWALK = "BattleOnTheBoardwalk"
BLUESHIFT           = "BlueShift"
CATALYST            = "Catalyst"
CERULEAN_FALL       = "CeruleanFall"
DARKNESS_SANCTUARY  = "DarknessSanctuary"
DREAM_CATCHER       = "DreamCatcher"
FRACTURE            = "Fracture"
HIGH_SPIRIT_PLATFORM= "HighSpiritedPlatform" ### ???
HUILONG_ISLAND      = "HuilongIsland"
LABYRINTH           = "labyrinth" # maze?
LOST_AND_FOUND      = "LostAndFound"
PARASITE            = "Parasite"
REDISTRIBUTION      = "Redistribution"
REDSHIFT            = "RedShift"
TREASURE_TROVE      = "TreasureTrove"

mapNameTranslations = { # use byte representations to avoid requiring encodings
    ##### CHINESE #####
    b'\xff\xfe1\x006\x00MO)Y\xafhHr'                                                        : _16BIT,
    b'\xff\xfe1\x006\x00MOCQ)Y\xafhHr'                                                      : _16BIT,
    b'\xff\xfe:_x\x91\xe5]\x82S)Y\xafhHr'                                                   : ACID_PLANT,
    b'\xff\xfe\x10\x90\xa6hKN0W)Y\xafhHr'                                                   : BATTLE_ON_BOARDWALK,
    b'\xff\xfe\xdd\x84\xfby)Y\xafhHr'                                                       : BLUESHIFT,
    b'\xff\xfe\x00\x7f\xdd\x84\xcby\x9fS)Y\xafhHr'                                          : BLUESHIFT,
    b'\xff\xfe\xd1\x9e\x97fV\x80\xbfk)Y\xafhHr'                                             : DARKNESS_SANCTUARY,
    b'\xff\xfe\xd1\x9e\x97f\x7f\x90\xbe\x96@b)Y\xafhHr'                                     : DARKNESS_SANCTUARY,
    b'\xff\xfeUc"Y\xb2})Y\xafhHr'                                                           : DREAM_CATCHER,
    b'\xff\xfe7_x\x91\xe5]\xe0^)Y\xafhHr'                                                   : DREAM_CATCHER,
    b'\xff\xfeH\x00u\x00i\x00l\x00o\x00n\x00g\x00I\x00s\x00l\x00a\x00n\x00d\x00'            : HUILONG_ISLAND,
    b'\xff\xfe0W\x99\x9f\x9b\\)Y\xafhHr'                                                    : HUILONG_ISLAND,
    b'\xff\xfeGl\x99\x9f\x9b\\)Y\xafhHr'                                                    : HUILONG_ISLAND,
    b'\xff\xfe0b\x0fa\xd8\x9a\x02fKN\x83X)Y\xafhHr'                                         : HIGH_SPIRIT_PLATFORM,
    b'\xff\xfe1Y\x0c\x80\rY\x97_)Y\xafhHr'                                                  : LOST_AND_FOUND,
    b'\xff\xfe1Yir\xdbb\x18\x98)Y\xafhHr'                                                   : LOST_AND_FOUND,
    b'\xff\xfe\x05}\xfby)Y\xafhHr'                                                          : REDSHIFT,
    b'\xff\xfe\xa2~\xfby)Y\xafhHr'                                                          : REDSHIFT,
    ##### FRENCH #####
    b'\xff\xfe1\x006\x00b\x00i\x00t\x00s\x00E\x00C\x00'                                     : _16BIT,
    b'acid plant'                                                                           : ACID_PLANT,
    b'\xff\xfeR\x00i\x00v\x00a\x00g\x00e\x00s\x00b\x00l\x00e\x00u\x00s\x00E\x00C\x00'       : BLUESHIFT,
    b'\xff\xfeR\x00i\x00v\x00a\x00g\x00e\x00s\x00b\x00l\x00e\x00u\x00s\x00E\x00C\x00'       : BLUESHIFT,
    b'\xff\xfeC\x00a\x00t\x00a\x00l\x00y\x00s\x00e\x00u\x00r\x00E\x00C\x00'                 : CATALYST,
    b'\xff\xfeS\x00a\x00n\x00c\x00t\x00u\x00a\x00i\x00r\x00e\x00d\x00e\x00s\x00t\x00\xe9\x00n\x00\xe8\x00b\x00r\x00e\x00s\x00E\x00C\x00'
                                                                                            : DARKNESS_SANCTUARY,
    b'\xff\xfeA\x00t\x00t\x00r\x00a\x00p\x00e\x00r\x00\xea\x00v\x00e\x00s\x00E\x00C\x00'    : DREAM_CATCHER,
    b'\xff\xfeD\x00\xe9\x00d\x00a\x00l\x00e\x00E\x00C\x00'                                  : LABYRINTH,
    b'\xff\xfe\\\xb8\xa4\xc2\xb8\xd2d\xc5\x0c\xd3\xb4\xc6\xdc\xb4\x98\xb7T\xb3'             : LOST_AND_FOUND,
    b'\xff\xfeP\x00a\x00r\x00a\x00s\x00e\x00r\x00r\x00e\x00s\x00E\x00C\x00'                 : PARASITE,
    b'\xff\xfeN\x00u\x00a\x00n\x00c\x00e\x00s\x00d\x00e\x00r\x00o\x00u\x00g\x00e\x00E\x00C\x00' : REDSHIFT,
    ##### GERMAN #####
    b'\xff\xfe1\x006\x00b\x00i\x00t\x00\xf3\x00w\x00E\x00R\x00'                             : _16BIT,
    b'\xff\xfeC\x00h\x00e\x00m\x00i\x00e\x00w\x00e\x00r\x00k\x00'                           : ACID_PLANT,
    b'\xff\xfeK\x00a\x00t\x00a\x00l\x00y\x00s\x00e\x00'                                     : CATALYST,
    b'\xff\xfeK\x00a\x00t\x00a\x00l\x00i\x00z\x00a\x00t\x00o\x00r\x00E\x00R\x00'            : CATALYST,
    b'\xff\xfeD\x00u\x00n\x00k\x00l\x00e\x00s\x00R\x00e\x00f\x00u\x00g\x00i\x00u\x00m\x00'  : DARKNESS_SANCTUARY,
    b'\xff\xfeT\x00r\x00a\x00u\x00m\x00f\x00\xe4\x00n\x00g\x00e\x00r\x00'                   : DREAM_CATCHER,
    b'\xff\xfeF\x00r\x00a\x00k\x00t\x00u\x00r\x00'                                          : FRACTURE,
    b'\xff\xfeF\x00u\x00n\x00d\x00g\x00r\x00u\x00b\x00e\x00'                                : TREASURE_TROVE,
    b'\xff\xfeT\x00r\x00e\x00a\x00s\x00u\x00r\x00e\x00T\x00r\x00o\x00v\x00e\x00'            : TREASURE_TROVE,
    ##### ITALIAN #####
    b'\xff\xfeI\x00m\x00p\x00i\x00a\x00n\x00t\x00o\x00c\x00h\x00i\x00m\x00i\x00c\x00o\x00'  : ACID_PLANT,
    b'\xff\xfeC\x00a\x00t\x00a\x00l\x00i\x00z\x00z\x00a\x00t\x00o\x00r\x00e\x00'            : CATALYST,
    b"\xff\xfeS\x00a\x00n\x00t\x00u\x00a\x00r\x00i\x00o\x00d\x00e\x00l\x00l\x00'\x00O\x00s\x00c\x00u\x00r\x00i\x00t\x00\xe0\x00"
                                                                                            : DARKNESS_SANCTUARY,
    b'\xff\xfeA\x00c\x00c\x00h\x00i\x00a\x00p\x00p\x00a\x00s\x00o\x00g\x00n\x00i\x00'       : DREAM_CATCHER,
    b'\xff\xfeS\x00t\x00r\x00a\x00d\x00e\x00p\x00e\x00r\x00d\x00u\x00t\x00e\x00'            : LOST_AND_FOUND,
    ##### KOREAN #####
    b'\xff\xfe1\x006\x00D\xbe\xb8\xd2\x98\xb7T\xb3'                                         : _16BIT,
    b'\xff\xfe`\xc5(\xc5\xdc\xb4\x0c\xd5\x9c\xb7\xb8\xd2\x98\xb7T\xb3'                      : ACID_PLANT,
    b'\xff\xfe\x14\xbe\xe8\xb8\xdc\xc2\x04\xd5\xb8\xd2'                                     : BLUESHIFT,
    b'\xff\xfet\xce\xc8\xd0\xac\xb9\xa4\xc2\xb8\xd2\x98\xb7T\xb3'                           : CATALYST,
    b'\xff\xfe8\xc1\xf0\xb8\xac\xb9H\xc5\xf4\xd3'                                           : CERULEAN_FALL,
    b'\xff\xfe\xdc\xb4\xbc\xb9\x90\xce\x98\xcc\x98\xb7T\xb3'                                : DREAM_CATCHER,
    b'\xff\xfe\xe4\xb2l\xd0\xc8\xb2\xa4\xc2\xdd\xc0\x04\xce\xb4\xc5\xac\xb9\x98\xb7T\xb3'   : DARKNESS_SANCTUARY,
    b'\xff\xfe\x04\xd5\x99\xb7\x98\xcc'                                                     : FRACTURE,
    b'\xff\xfe\x0c\xd3|\xb7\xac\xc0t\xc7\xb8\xd2'                                           : PARASITE,
    b'\xff\xfe\x08\xb8\xdc\xb4l\xc2\x04\xd5\xb8\xd2\x98\xb7T\xb3'                           : REDSHIFT,
    ##### POLISH #####
    b'\xff\xfeW\x00y\x00t\x00w\x00\xf3\x00r\x00n\x00i\x00a\x00K\x00w\x00a\x00s\x00u\x00E\x00R\x00'
                                                                                            : ACID_PLANT,
    b'\xff\xfeB\x00l\x00u\x00e\x00s\x00h\x00i\x00f\x00t\x00E\x00E\x00'                      : BLUESHIFT,
    b'\xff\xfeS\x00a\x00n\x00k\x00t\x00u\x00a\x00r\x00i\x00u\x00m\x00M\x00r\x00o\x00k\x00u\x00E\x00R\x00'
                                                                                            : DARKNESS_SANCTUARY,
    b'\xff\xfeK\x00a\x00t\x00a\x00l\x00y\x00s\x00e\x00'                                     : CATALYST,
    b'\xff\xfeA\x01a\x00p\x00a\x00c\x00z\x00S\x00n\x00\xf3\x00w\x00E\x00R\x00'              : DREAM_CATCHER,
    b'\xff\xfeZ\x00a\x00g\x00u\x00b\x00i\x00o\x00n\x00e\x00D\x00r\x00o\x00g\x00i\x00E\x00R\x00' : LOST_AND_FOUND,
    b'\xff\xfeP\x00o\x00c\x00z\x00e\x00r\x00w\x00i\x00e\x00n\x00i\x00e\x00n\x00i\x00e\x00E\x00R\x00' : REDSHIFT,
    ##### RUSSIAN #####
    b'\xff\xfe1\x006\x001\x048\x04B\x04 \x04\x12\x04'                                       : _16BIT,
    b'\xff\xfe\x1a\x048\x04A\x04;\x04>\x04B\x04=\x04K\x049\x047\x040\x042\x04>\x044\x04 \x04\x12\x04'
                                                                                            : ACID_PLANT,
    b'\xff\xfe!\x048\x04=\x045\x045\x04A\x04<\x045\x04I\x045\x04=\x048\x045\x04 \x04\x12\x04': BLUESHIFT,
    b'\xff\xfe\x1b\x040\x047\x04C\x04@\x04=\x04K\x045\x04C\x04B\x045\x04A\x04K\x04 \x04\x12\x04' : BLUESHIFT,
    b'\xff\xfe\x1a\x040\x04B\x040\x04;\x048\x047\x040\x04B\x04>\x04@\x04 \x04\x12\x04'      : CATALYST,
    b'\xff\xfe!\x042\x04O\x04B\x048\x04;\x048\x04I\x045\x04B\x04L\x04<\x04K\x04 \x04\x12\x04' : DARKNESS_SANCTUARY,
    b'\xff\xfe\x1b\x04>\x042\x045\x04F\x04A\x04=\x04>\x042\x04 \x04\x12\x04'                : DREAM_CATCHER,
    b'\xff\xfe\x11\x04N\x04@\x04>\x04=\x040\x04E\x04>\x044\x04>\x04:\x04 \x04\x12\x04'      : LOST_AND_FOUND,
    b'\xff\xfe\x1a\x04@\x040\x04A\x04=\x04>\x045\x04A\x04<\x045\x04I\x045\x04=\x048\x045\x04 \x04\x12\x04'
                                                                                            : REDISTRIBUTION,
    ##### SPANISH #####
    b'\xff\xfeP\x00l\x00a\x00n\x00t\x00a\x00\xe1\x00c\x00i\x00d\x00a\x00E\x00E\x00'         : ACID_PLANT,
    b'\xff\xfeP\x00l\x00a\x00n\x00t\x00a\x00\xe1\x00c\x00i\x00d\x00a\x00E\x00J\x00'         : ACID_PLANT,
    #b'\xff\xfeC\x00o\x00r\x00r\x00o\x00s\x00i\x00o\x00n\x00E\x00C\x00'                      : ACID_PLANT,
    b'\xff\xfeC\x00a\x00t\x00a\x00l\x00i\x00z\x00a\x00d\x00o\x00r\x00E\x00J\x00'            : CATALYST,
    b'\xff\xfeC\x00a\x00t\x00a\x00l\x00i\x00z\x00a\x00d\x00o\x00r\x00E\x00E\x00'            : CATALYST,
    b'\xff\xfeC\x00a\x00\xed\x00d\x00a\x00c\x00e\x00r\x00\xfa\x00l\x00e\x00a\x00E\x00E\x00' : CERULEAN_FALL,
    b'\xff\xfeO\x00t\x00o\x00\xf1\x00o\x00c\x00e\x00r\x00\xfa\x00l\x00e\x00o\x00E\x00J\x00' : CERULEAN_FALL,
    b'\xff\xfeA\x00u\x00t\x00o\x00m\x00n\x00e\x00c\x00\xe9\x00r\x00u\x00l\x00\xe9\x00e\x00n\x00E\x00C\x00' : CERULEAN_FALL,
    b'\xff\xfeS\x00a\x00n\x00t\x00u\x00a\x00r\x00i\x00o\x00d\x00e\x00l\x00a\x00o\x00s\x00c\x00u\x00r\x00i\x00d\x00a\x00d\x00E\x00E\x00'
                                                                                            : DARKNESS_SANCTUARY,
    b'\xff\xfeS\x00a\x00n\x00t\x00u\x00a\x00r\x00i\x00o\x00d\x00e\x00l\x00a\x00o\x00s\x00c\x00u\x00r\x00i\x00d\x00a\x00d\x00E\x00J\x00'
                                                                                            : DARKNESS_SANCTUARY,
    b'\xff\xfeA\x00t\x00r\x00a\x00p\x00a\x00s\x00u\x00e\x00\xf1\x00o\x00s\x00E\x00E\x00'    : DREAM_CATCHER,
    b'\xff\xfeA\x00t\x00r\x00a\x00p\x00a\x00s\x00u\x00e\x00\xf1\x00o\x00s\x00E\x00J\x00'    : DREAM_CATCHER,
    b'\xff\xfeF\x00r\x00a\x00c\x00t\x00u\x00r\x00a\x00E\x00J\x00'                           : FRACTURE,
    b'\xff\xfeF\x00r\x00a\x00c\x00t\x00u\x00r\x00a\x00E\x00E\x00'                           : FRACTURE,
    b'\xff\xfeO\x00b\x00j\x00e\x00t\x00o\x00s\x00p\x00e\x00r\x00d\x00i\x00d\x00o\x00s\x00E\x00E\x00'    : LOST_AND_FOUND,
    b'\xff\xfeA\x00c\x00h\x00a\x00d\x00o\x00s\x00e\x00P\x00e\x00r\x00d\x00i\x00d\x00o\x00s\x00'         : LOST_AND_FOUND,
    b'\xff\xfeP\x00a\x00r\x00a\x00S\x00i\x00t\x00o\x00E\x00E\x00'                           : PARASITE,
    b'\xff\xfeR\x00o\x00j\x00o\x00a\x00m\x00a\x00n\x00e\x00c\x00e\x00r\x00E\x00J\x00'       : REDSHIFT,
    ##### UNKNOWN #####
    b'\xff\xfe1\x006\x00B\x00i\x00t\x00s\x00'                                               : _16BIT,
    b'\xff\xfe1\x006\x00b\x00i\x00t\x00s\x00E\x00E\x00'                                     : _16BIT,
    b'\xff\xfe1\x006\x00b\x00i\x00t\x00s\x00E\x00J\x00'                                     : _16BIT,
    b'\xff\xfeU\x00s\x00i\x00n\x00a\x00\xc1\x00c\x00i\x00d\x00a\x00'                        : ACID_PLANT,
    b'\xff\xfeC\x00o\x00r\x00r\x00o\x00s\x00i\x00o\x00n\x00E\x00C\x00'                      : ACID_PLANT,
    b'\xff\xfeD\x00e\x00s\x00v\x00i\x00o\x00p\x00a\x00r\x00a\x00o\x00A\x00z\x00u\x00l\x00'  : BLUESHIFT,
    b'\xff\xfeF\x00r\x00a\x00c\x00t\x00u\x00r\x00e\x00'                                     : FRACTURE,
    b'\xff\xfeH\x00i\x00g\x00h\x00S\x00p\x00i\x00r\x00i\x00t\x00e\x00d\x00P\x00l\x00a\x00t\x00f\x00o\x00r\x00m\x00'
                                                                                            : HIGH_SPIRIT_PLATFORM,
    b'\xff\xfel\x00a\x00b\x00y\x00r\x00i\x00n\x00t\x00h\x00'                                : LABYRINTH,
    b'\xff\xfeL\x00a\x00b\x00e\x00r\x00i\x00n\x00t\x00o\x00E\x00J\x00'                      : LABYRINTH,
    b'\xff\xfeP\x00a\x00r\x00a\x00S\x00i\x00t\x00e\x00'                                     : PARASITE,
    b'\xff\xfeR\x00e\x00d\x00i\x00s\x00t\x00r\x00i\x00b\x00u\x00t\x00i\x00o\x00n\x00'       : REDISTRIBUTION,
    b'\xff\xfeD\x00e\x00s\x00v\x00i\x00o\x00p\x00a\x00r\x00a\x00o\x00V\x00e\x00r\x00m\x00e\x00l\x00h\x00o\x00' : REDSHIFT,
    b'\xff\xfeR\x00e\x00d\x00s\x00h\x00i\x00f\x00t\x00E\x00E\x00'                           : REDSHIFT,
    b'\xff\xfeR\x00o\x00t\x00s\x00t\x00i\x00c\x00h\x00'                                     : REDSHIFT,
}
for k,v in list(mapNameTranslations.items()): # convert byte representation into str
    newKey = k.decode('utf-16')
    mapNameTranslations[newKey] = v
    del mapNameTranslations[k]


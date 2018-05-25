
# Recommended Usage -- Non-Python

While your code does not need to run in python, currently it must invoke a
a new process using the `python` command.  Once installed, prove its successful
installation by invoking the --help option on the command line.

```shell
$ python -m sc2gameMapRepo --help
usage:  [-h] [--list] [--details] [--path] [--mapname MAPNAME] [--exclude]
        [--best] [--ladder LADDER] [--combat COMBAT] [--economy ECONOMY]
        [--scenario SCENARIO] [--misc MISC] [--test TEST] [--year YEAR]
        [--season {1,2,3,4}] [--mode {1v1,2v2,3v3,4v4}]

optional arguments:
  -h, --help            show this help message and exit
  --list                Display all known maps by category.
  --details             show details of each mapname.
  --path                provide the absolute path to the file
  --mapname MAPNAME     the name of the specific map to load.
  --exclude             exclude maps with names specified by --mapname.
  --best                match maps that are closer with --mapname
  --ladder LADDER       ladder must be selected (True) or ignored.
  --combat COMBAT       combat maps must be selected (True) or ignored.
  --economy ECONOMY     economy maps must be selected (True) or ignored.
  --scenario SCENARIO   single-player games with a specific objective to
                        achieve must be selected (True) or ignored.
  --misc MISC           misc maps must be seleced (True) or ignored.
  --test TEST           test maps must be seleced (True) or ignored.
  --year YEAR           the calendar year the ladder season occurred.
  --season {1,2,3,4}    the specific ladder season within a calendar year.
  --mode {1v1,2v2,3v3,4v4}
                        the official ladder category to play.
```

Without any other language interface implemented, the best way to retrieve map
information is to issue a system command and parse STDOUT for the queried info.

### Parameter Categories

Reference `--help` for details on paramater usage.

1. main routine behavior : _force handling of results to print desired data_
* `--list`
* `--details`
* `--path`

2. map name matching criteria : _match the maps whose name follow the criteria_
* `--mapname`
* `--exclude`
* `--best`

> **TIP** the value of `--mapname` can be a python regular expression.
> 
> **TIP** `--best` has two potential behaviors.
> 1. if mapname is specified, selection favors mapnames that more closely match the specified name (shortest name).
> 2. if mapname is not specified, a map is selected at random.

3. map attribute criteria : _match the maps whose attributes follow the criteria_
* `--ladder`
* `--combat`
* `--scenario`
* `--misc`
* `--test`
* `--season`
* `--mode`

**IMPORTANT**: non-python users are restricted to these attributes.  `__main__.py`
must be updated if additional attributes are desired.

### Positive or Negative Assertion

Each attribute be positively asserted (match the specified value) or negatively
asserted (match all values that do not match the specified value).  When
specifying an attribute, an empty `""` or `0` value will negatively assert
the attribute whereas other values positively assert matching.

### Examples

##### Linux and/or Windows

EXAMPLE: find the absolute path of all 2018, season2 ladder maps. 
```shell
$ python sc2gameMapRepo --ladder=True --year=2018 --season=2 --path
```
```
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\16BitLE.SC2Map
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\AcidPlantLE.SC2Map
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\CatalystLE.SC2Map
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\DarknessSanctuaryLE.SC2Map
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\DreamcatcherLE.SC2Map
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\LostAndFoundLE.SC2Map
<InstallPath>\sc2gameMapRepo\Maps\Ladder\mode1v1\year2018\Season2\RedshiftLE.SC2Map
```

EXAMPLE: find the names of all that contain `marine` in the name and are tagged
in a `scenario` subfolder.
```shell
$ python sc2gameMapRepo --mapname=marine --combat=True
```
```
Banshee2vsMarine8
Banshee4vsMarine16
Banshee4vsMarine16Medivac1
```

EXAMPLE: select the 'best' `season 1` map
> NOTE: the matching map pool includes ladders maps from season 1 of both 2017 and 2018.
> NOTE: the map is selected at random so the result may vary.
```shell
$ python sc2gameMapRepo --season=1 --best
```
```
Blackpink
```

EXAMPLE: show map attribute details for all maps with `acid` in their name.
> NOTE: notice in this case that the same map was listed twice, but correctly
> distinguished them as belonging to both seasons 1 and 2.
```shell
$ python sc2gameMapRepo --mapname=acid --details
```
```
<MapRecord "AcidPlant">
        path : <InstallPath>/sc2gameMapRepo/Maps/Ladder/mode1v1/year2018/Season1/AcidPlantLE.SC2Map
      ladder : True
        mode : 1v1
        year : 2018
      season : 1
<MapRecord "AcidPlant">
        path : <InstallPath>/sc2gameMapRepo/Maps/Ladder/mode1v1/year2018/Season2/AcidPlantLE.SC2Map
      ladder : True
        mode : 1v1
        year : 2018
      season : 2
Found 2 maps that match given criteria.
```

##### MacOS / OSX

Not tested on Apple (R) OS, but it *should* work just fine. :)

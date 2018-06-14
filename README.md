[![Coverage Status](https://coveralls.io/repos/github/mikemhenry/sc2gameMapRepo/badge.svg?branch=tests)](https://coveralls.io/github/mikemhenry/sc2gameMapRepo?branch=tests)

[![Build Status](https://travis-ci.org/mikemhenry/sc2gameMapRepo.svg?branch=master)](https://travis-ci.org/mikemhenry/sc2gameMapRepo)

# Starcraft2 Maps with Simple, Universal Retrieval 

---
## About

The objective of this repository is to consolidate known Starcraft2 (SC2) maps
for use by developers creating bots, AI agents or some other custom code
project.

#### Simple. Effective. Useful.   

The implementation of this code base is intended to not only consolidate SC2
maps into a single location, but also provide a simple interface to reliably
access and use basic map information.  This includes selecting a map for
play (optionally specifying user-defined criteria), easily identify the .SC2Map
file absolute path, identify automatically generated tags that describe the
map(s) and identify any collection of maps using keywords to describe the map.

The intent is to provide a minimal (*simple!*) interface so that new-commers
can easily use developed functionality. This small project, independent of
other code, should prove more reliable to retrieve desired map information
(*effective!*). By being simple and effective, hopefully this repository proves
helpful to new and existing SC2 AI developers (*useful!*). 

#### Rationale: Why Create this Repository?

* One, single location where many SC2 AI-relevant maps are accumulated.  No need to use mutliple user's repositories with their own map management systems.
* OS/installation independent.  This package manages the maps itself without the user needing to install them at a particular location.
* Remove the burden from the user to have to know where to install the maps so their SC2 client can find the maps.
* SC2 map editor does not appear to be compatible non-Blizzard code to programmatically extract relevant .SC2Map information.

#### Functional Overview

All .SC2Map files are located within the `Maps` subfolder or subsequent
subfolders. Each subsequent subfolder encodes an attribute that describes all
subsequent .SC2Map files contained within it or its subfolders. Using this
format, an index file that maps attribute tags to filenames is not needed.

This repository does not prevent potential .SC2Map file redundancy.  Instead,
this storage approach allows files to be _very easily_ added into the repo w/o
having to additionally maintain a mapping file for each new file that's added.
Allowing duplicates also allows multiple versions of the same file to exist
within the repository, granted each file will have a unique set of automatic-
generated attribute tags to distinguish between them.

When searching for maps given user-defined, by first restricting which maps are
examined by first matching attributes first and then the map name, if specified. 

The current implementation performs the lookup [O(n)](https://en.wikipedia.org/wiki/Big_O_notation) time where N is the number
of maps managed within the repository.  If N becomes large, this may need to
be optomized further for timely lookups.

---
## Installation

#### Dependencies

This package is mostly self-contained with only one external package
dependency: [six](https://pypi.org/project/six/) (python2 and python 3 compatibility)

#### Instructions

1. Install any(?) version of [python](https://www.python.org/downloads/) and use [pip](https://pypi.org/project/pip/) to install [six](https://pypi.org/project/six/).
2. git clone https://github.com/ttinies/sc2gameMapRepo (or fork and clone your repo).
> NOTE: to ensure the destination is visible by your project, consider the following strategies:
> * install this package within your own project
> * add `<destination>` to the environment variable: `PYTHONPATH`
> * `.../<Python folder>/Lib/site-packages/sc2gameMapRepo/` (similar to what a pip install would do)

**TIP**: adding sc2gameMapRepo to the system path using the %PYTHONPATH% variable
can help python locate your sc2gameMapRepo installation.

---
## Recommended Usage

Refer to [python](/blob/master/USAGE_PUTHON.md)-specific or [non python](/blob/master/USAGE_NON_PYTHON.md)-specific usage documents.

---
## Troubleshooting

In the event that a map request issued by no matching map is found, an
`InvalidMapSelection` Exception is raised.  If encountered, your query must be
revised to properly select maps.

> EXAMPLE: given criteria `Foo=True` results in an exception because none of the
> maps exist in a subfolder named `foo` (ignoring folder's case).

`sc2gameMapRepo.constants.InvalidMapSelection: could not find any matching maps given criteria: {'foo': True}`

> EXAMPLE: given criteria `year=2017` and `Combat=True`, an exception is raised
> because none of the maps exist in a subfolder structure with both of these
> attributes in the path.

`sc2gameMapRepo.constants.InvalidMapSelection: could not find any matching maps given criteria: {'year': 2017, 'Combat': True}`

---
## Further Development and Augmentation

#### Add New Maps?

New .SC2Map files need to be added to the `Maps` subfolder.  The files can be
placed in any subfolder structure the user desires.  Each subfolder represents
an attribute that describes every map file it contains, including its own
subfolders.  The folder name is deemed case-insensitive for the purpose of
attribute identification.

The subfolder name is interpreted in one of two ways according to its format:
1. non-numeric chars mean the attribute is interpreted with a `bool` value.
2. if a numeric char is included, that char signals the beginning of an `int` or `string` typed value.

> EXAMPLE: a hypothetical folder, `MaxPlayers6`, would be interpreted with an
> attribute name `maxplayers` with an `int` value `6`.

> EXAMPLE: all .SC2Map files within this subfolder are `Ladder` maps. 

`/Maps/Economy/`

> EXAMPLE: all .SC2Map files within this subfolder are official `Ladder` maps
> which are 1v1 maps released in 2018. 

`/Maps/Ladder/mode1v1/year2018`

#### Add New Features to the Code?

This is an open-use repository.  Feel free to fork and issue pull requests.

However, changing the defined interface is discouraged in order to promote
backward compatibility.  Valuable feature enhancements and bug fixes are
welcome.

###### Anticipated Useful, To-Be-Developed Features

* Automated testing of package functionality.
* Additional language-specific interfaces beyond Python.
* package management support: [PyPi](https://pypi.org/) / [pip](https://pypi.org/project/pip/) and [conda](https://www.anaconda.com/what-is-anaconda/).
* Accomodations for unforseen/unhandled incompatibility issues.

---
## Credits for Single-Player Scenario author/GitHub Repositories:

Many scenarios have already been created that involve having a single agent
solve a specifically defined task.  These are included within this repository
too for completeness.

* DeepMind [PYSC2](https://github.com/deepmind/pysc2/blob/master/README.md)
* SoyGema  [pySC2_minigames](https://github.com/SoyGema/pySC2_minigames/blob/master/README.md)
* SoyGema  [Startcraft_pysc2_minigames](https://github.com/SoyGema/Startcraft_pysc2_minigames)
* SoyGema  [minigames_pysc2](https://github.com/SoyGema/minigames_pysc2)
* 4rChon   [sc2-ai-mini-games](https://github.com/4rChon/sc2-ai-mini-games/blob/master/README.md)


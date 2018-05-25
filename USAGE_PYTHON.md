
# Recommended Usage -- Python

This implementation supports both python2 and python3.

Indexing the maps occurs at run-time only the first time a map selection
request occurs, following the principle of [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation).  The
results are cached such that any subsequent calls utilize the prior results.

**IMPORTANT**: rather than returning text/strings of the information (like the
non-python implementation does), the python implementation returns `MapRecord`
objects.

### Parameter Categories

```python
def selectMap(name=None, excludeName=False, closestMatch=True, **tags)
```

1. map name matching criteria : _match the maps whose name follow the criteria_
* `name` (default=None)
> a text string used as a regex to match the map filename.
* `excludeName` (default=False)
> whether matching map names are included (False) or excluded (True).
> only enforced if name is also specified
* `closestMatch` (default=True)
> force selection among the map pool that matches attribute criteria or by name.

**TIP** the value of `mapname` can be a python regular expression.

**TIP** `closestMatch` has two potential behaviors.
> 1. if mapname is specified, selection favors mapnames that more closely match
> > the specified name (shortest name).
> 2. if mapname is not specified, a map is selected at random.

2. `tags` attribute criteria : _match the maps whose attributes follow the criteria_
* any key:value pair as criteria
> match criteria against map attributes.

### positive or negative assertion

Each attribute be positively asserted (match the specified value) or negatively
asserted (match all values that do not match the specified value).  When
specifying an attribute, an empty `""` or `0` value will negatively assert
the attribute whereas other values positively assert matching.

### Examples

EXAMPLE: import the package's functionality
```python
from sc2gameMapRepo import selectMap
```

EXAMPLE: retrieve all melee maps that do not contain "flat" in their name and
> print their attribute keys.
```python
for m in selectMap(name="flat", melee=True, excludeName=True, closestMatch=False):
    print(m, m.attrs)
```
> *
<MapRecord "Simple128"> ['path', 'melee']
<MapRecord "Simple64"> ['path', 'melee']
<MapRecord "Simple96"> ['path', 'melee']
*

EXAMPLE: select the 2017 map that best matches the name 'f'.
> NOTE: map `Frost` is always selected; no randomness with current map set.
```python
print(selectMap(name="f", year=2017, closestMatch=True))
```
> *
<MapRecord "Frost">
*

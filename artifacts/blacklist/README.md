## Pipelines
Our code can be partitioned into 4 logical units:

Preprocessor: Clone the repo, find out the suitable commit version pair of the repo (old, new). 

API collectors: 

1. Collect all the public APIs

2. public API classification (added, removed, deprecated, param chaned, return changed, safed)

FileOperation Manager: since we have a lot file operations, like parsing and git operation, it is 
safe to have a separate module to manage the files 

AST Manager: same as the file manager, we have a lot separate and reuseable AST apis, it is safe to create a manager
for those apis 

## Interfaces 

The Preprocessor only clone the repo, and find the suitable version commit number, then create and return the pair (old,new)

API collectors have two purpose:

1. Collect all public APIs. Based on our current approach, we ask the File Manager to find all the files end with .py, return a list of file path. Then we ask AST manager to find the nodes with "_all_" in those files, return the API list. Then it should create and return a map that maps a (publicAPI, PathForAPI) for a given git version(new/old)

2. Public API classification: Based on the map created in the public API, it ask diffrent logic unit to classify the corresponding APIs. 



## How to use 

the `test.py` in the engine will execute the cloning and testing automatically 
modify the package list in the file and run `python3 test.py`


code structure:
`Preprocessor.py`

`APICollector.py` will find all public APIs, and run different units to find added, removed, etc

`FileManager.py`

`ASTManager.py` 

`getAddedAPI.py`

`getRemovedAPI.py`

`getDeprecatedAPI.py` 

`formatter.sh` will formatting all the files using `black` package in the `ls` files 


`old` dir contains the the useless code written before


## Questions in API

1. Q: The finding commit sha takes a long time, but the commit sha will not change every time run the program. 
Solution: we can create a map in the files, and look up the commit sha every time we run the program, if it is not in the map, we run the find_commit method 


2. Q: in the find deprecate files, the method `check_ALL_flag` will return true if find **at least** one `_all_` export symbol, is this method reliable? 




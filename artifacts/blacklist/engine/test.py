# Test for Blacklist
import os
from datetime import datetime
import argparse


from FileManager import FileManager
from Preprocessor import Preprocessor
from APICollector import APICollector
from ASTManager import ASTManager


# Adding the argument for debugging purpose
parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--verbose", action="store_true", help="echo the procedural outout"
)
args = parser.parse_args()

# Passing the debug mode
DEBUG = args.verbose
if args.verbose:
    print("Verbose mode on!")

# declare test packages:  {owner, name, githublink, startdate, enddate}
test_package = [
    (
        "networkx",
        "networkx",
        "https://github.com/networkx/networkx.git",
        datetime(2022, 1, 22),
        datetime(2023, 4, 3),
    )
]

# download the test package and change dir to `~/tests`
print("...Preparing the repo....\n")
download_path = "~/tests"
if os.path.exists(os.path.expanduser(download_path)):
    pass
else:
    os.system("mkdir " + download_path)
os.chdir(os.path.expanduser("~/tests"))
path = os.getcwd()
print("...Current package downloading directory is: ", os.getcwd())


# test the program
for owner, name, link, start, end in test_package:
    # initiate the instances
    fm = FileManager(path, name, link, DEBUG)
    pre = Preprocessor(owner, name, DEBUG)
    am = ASTManager()
    api_collector = APICollector(name, fm, am, pre, start, end, DEBUG)

    # get the added api
    added_apis = api_collector.getAddedApis()
    removed_apis = api_collector.getRemovedApis()
    param_changed_apis = api_collector.getParamChangedApis()
    return_changed_apis = api_collector.getReturnChangedApis()
    deprecated_apis = api_collector.getDeprecatedApis()
    fm.store_apis(
        added_apis,
        removed_apis,
        param_changed_apis,
        return_changed_apis,
        deprecated_apis,
    )

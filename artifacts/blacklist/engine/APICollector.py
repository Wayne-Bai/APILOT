import os
from datetime import datetime
import sys
import re
from typing import Dict

# import pickle

from ASTManager import ASTManager
from Preprocessor import Preprocessor
from FileManager import FileManager


"""
Module: API collector
Function: middle end of processing, using ast tree and file operations to collect the apis
"""


class APICollector:
    def __init__(self, repo_name, fm, am, pre, start_date, end_date, DEBUG) -> None:
        self.repo_name = repo_name
        self.fm = fm
        self.am = am
        self.pre = pre
        self.debug_mode = DEBUG

        # identify the flag for the api collection
        self.all_flag = self.getAllFlag()

        if self.debug_mode:
            print("\nStarting collect the api for package: ", self.repo_name)
            print("\nDoes current repo has the all flag? :", self.all_flag)

        # get the commit id
        self.old_commitId = pre.getCommitId(start_date)
        self.new_commitId = pre.getCommitId(end_date)

        # get the apis map
        self.old_pub_apis_map = self.getOldPubApiMap()
        self.new_pub_apis_map = self.getNewPubApiMap()

        # get the apis
        self.old_pub_apis = set(self.getOldPubApiMap().keys())
        self.new_pub_apis = set(self.getNewPubApiMap().keys())

        return

    """
    identify the __all__ flag in the current repo
    the scope for the flag applys for the while repo, instead of a single file!
    """

    def getAllFlag(self) -> bool:
        all_py_file = self.fm.findAllPyFile()
        for f in all_py_file:
            source = self.fm.load_file(f)

            # if one of the file has the flag
            # then it is true
            if self.am.hasAllFlag(source):
                return True

        return False

    """
    find all apis in the repo
    understore prefix indicates only be called within the class
    """

    def _find_all_apis(self) -> Dict[str, str]:
        API_map = {}
        all_py_file = self.fm.findAllPyFile()
        for f in all_py_file:
            source = self.fm.load_file(f)
            deflist = self.am.collectFuncAndClass(source)
            for definition in deflist:
                API_map[str(definition)] = str(os.path.relpath(f, self.fm.repo_path))

        if self.debug_mode:
            print("Found the total public apis: ", len(API_map), "\n")

        return API_map

    """
    find all public python apis (in the __all__) in the repo
    """

    def find_pub_apis(self) -> Dict[str, str]:
        API_map = {}

        # return all the api if no _all_ flag is occured in the repo
        if self.all_flag == False:
            return self._find_all_apis()

        all_py_file = self.fm.findAllPyFile()
        for f in all_py_file:
            source = self.fm.load_file(f)
            deflist = self.am.getExternalApis(source)
            for definition in deflist:
                # map to the relative path
                API_map[str(definition)] = str(os.path.relpath(f, self.fm.repo_path))

        if self.debug_mode:
            print("Found the total public apis: ", len(API_map), "\n")

        return API_map

    """
    get the apis in difference commits
    """

    def getOldPubApiMap(self) -> set:
        self.fm.gitCheckOut(self.old_commitId)
        return self.find_pub_apis()

    def getNewPubApiMap(self) -> set:
        self.fm.gitCheckOut(self.new_commitId)
        return self.find_pub_apis()

    """
    by default will look up the new pub apis map to find path
    """

    def append_apis_path(self, apis, lookUpNew=True) -> str:
        result_list = []
        for api in apis:
            return_map = {}

            if lookUpNew == True:
                return_map["func_name"] = api
                return_map["path"] = self.new_pub_apis_map[api]
                file_src = self.fm.load_file(os.path.join(self.fm.repo_path, self.new_pub_apis_map[api]))
                return_map["parent"] = self.am.findParent(file_src, api)
                # return_map[api] = self.new_pub_apis_map[api]
            else:
                return_map["func_name"] = api
                return_map["path"] = self.old_pub_apis_map[api]
                file_src = self.fm.load_file(os.path.join(self.fm.repo_path, self.old_pub_apis_map[api]))
                return_map["parent"] = self.am.findParent(file_src, api)
                # return_map[api] = self.old_pub_apis_map[api]

            result_list.append(return_map)
        return result_list

    """
    get the corresponding apis: 5 types
    Added, Removed, Parameter Changed, Return Changed, Deprecated
    """

    def getAddedApis(self):
        AddedApis = []

        # get the new elements apis
        AddedApis = list(self.new_pub_apis - self.old_pub_apis)

        if self.debug_mode:
            print("total added API: ", len(AddedApis), "\n")
            print("Added APIs: ", AddedApis, "\n")

        self.fm.gitCheckOut(self.new_commitId)
        AddedApisLists = self.append_apis_path(AddedApis)

        return AddedApisLists

    def getRemovedApis(self):
        RemovedApis = []

        # get the new elements apis
        RemovedApis = list(self.old_pub_apis - self.new_pub_apis)

        if self.debug_mode:
            print("total removed API: ", len(RemovedApis), "\n")
            print("Removed APIs: ", RemovedApis, "\n")

        self.fm.gitCheckOut(self.old_commitId)
        RemovedApisLists = self.append_apis_path(RemovedApis, False)
        return RemovedApisLists

    def getParamChangedApis(self):
        ParamChangedApis = []

        # get the shared apis
        shared_apis = list(self.old_pub_apis & self.new_pub_apis)

        """
        the map may burnout the mem if the api is too many
        """

        # get the new apis map
        self.fm.gitCheckOut(self.new_commitId)
        api_map_new = self.find_pub_apis()
        # map {api : file_src}
        api_src_new = {}

        for new_api in shared_apis:
            if new_api in api_map_new:
                path = api_map_new[new_api]
                # load the file
                f_src = self.fm.load_file(os.path.join(self.fm.repo_path, path))
                api_src_new[new_api] = f_src

        # get the old apis map
        self.fm.gitCheckOut(self.old_commitId)
        api_map_old = self.find_pub_apis()
        # map {api : file_src}
        api_src_old = {}
        for old_api in shared_apis:
            if old_api in api_map_old:
                path = api_map_old[old_api]
                # load the file
                f_src = self.fm.load_file(os.path.join(self.fm.repo_path, path))
                api_src_old[old_api] = f_src

        # compare two file src
        for api in shared_apis:
            src_new = api_src_new[api]
            src_old = api_src_old[api]
            api_path = api_map_new[api]
            param_map = self.am.findParamChanged(api, src_old, src_new, api_path)
            if param_map != None:
                ParamChangedApis.append(param_map)

        if self.debug_mode:
            print("total parameter changed api: ", len(ParamChangedApis))
            print(
                "parameter changed apis: ",
                list(map(lambda x: x["func_name"], ParamChangedApis)),
            )
        return ParamChangedApis

    def getReturnChangedApis(self):
        ReturnChangedApis = []
        # get the shared apis
        shared_apis = list(self.old_pub_apis & self.new_pub_apis)

        """
        the map may burnout the mem if the apis are too many
        """

        # get the new apis map
        self.fm.gitCheckOut(self.new_commitId)
        api_map_new = self.find_pub_apis()
        # map {api : file_src}
        api_src_new = {}

        for new_api in shared_apis:
            if new_api in api_map_new:
                path = api_map_new[new_api]
                # load the file
                f_src = self.fm.load_file(os.path.join(self.fm.repo_path, path))
                api_src_new[new_api] = f_src

        # get the old apis map
        self.fm.gitCheckOut(self.old_commitId)
        api_map_old = self.find_pub_apis()
        # map {api : file_src}
        api_src_old = {}
        for old_api in shared_apis:
            if old_api in api_map_old:
                path = api_map_old[old_api]
                # load the file
                f_src = self.fm.load_file(os.path.join(self.fm.repo_path, path))
                api_src_old[old_api] = f_src

        # compare two file src
        for api in shared_apis:
            src_new = api_src_new[api]
            src_old = api_src_old[api]
            api_path = api_map_new[api]
            return_map = self.am.findReturnChanged(api, src_old, src_new, api_path)
            if return_map != None:
                ReturnChangedApis.append(return_map)

        ## API filter
        RetList = self.filterPrivateFunc(
            list(map(lambda x: x["func_name"], ReturnChangedApis))
        )

        if self.debug_mode:
            print("total return changed api after filtering: ", len(ReturnChangedApis))
            print(
                "return changed api before the filter: ",
                list(map(lambda x: x["func_name"], ReturnChangedApis)),
                "\n",
            )
            print("total return changed api after filtering: ", len(RetList))
            print("return changed apis after filtering: ", RetList)

        return ReturnChangedApis

    def getDeprecatedApis(self):
        DeprecatedApis = []
        # check out to the new version
        self.fm.gitCheckOut(self.new_commitId)

        all_py_file = self.fm.findAllPyFile()
        for f in all_py_file:
            source = self.fm.load_file(f)
            api_path = str(os.path.relpath(f, self.fm.repo_path))
            DeprecatedApis += self.am.findDeprecated(source, api_path)

        if self.debug_mode:
            print("total deprecated API: ", len(DeprecatedApis), "\n")
            print(
                "Deprecated APIs: ",
                list(map(lambda x: x["func_name"], DeprecatedApis)),
                "\n",
            )
        return DeprecatedApis

    """
    prune the api (function) under the class 
    """

    def filterPrivateFunc(self, apis) -> list:
        # get the file path
        API_map = self.find_pub_apis()
        filtered_apis = []
        print(apis)
        for api in apis:
            path = API_map.get(str(api))
            f_src = self.fm.load_file(os.path.join(self.fm.repo_path, path))
            parent = self.am.findParent(f_src, api)
            if parent == "Module":
                filtered_apis.append(api)
        return filtered_apis

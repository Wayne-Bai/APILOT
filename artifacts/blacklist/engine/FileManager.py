import os
from datetime import datetime
import sys
import re
from time import sleep
import json

"""
 Module: File Manager
 Function: Manage the all files, including downloading repo, git operations and directory/file operations 
"""


class FileManager:
    def __init__(self, path, name, link, DEBUG) -> None:
        # absolute path
        self.result_path = os.path.join(os.path.expanduser(path), "datasets")
        self.repo_path = os.path.join(os.path.expanduser(path), name)
        self.repo_name = name
        self.debug_mode = DEBUG
        self.download_link = link

        if self.debug_mode:
            print(
                "creating a file manager for: "
                + self.repo_name
                + " at path: "
                + self.repo_path
            )

        # creating the result repo
        if os.path.exists(os.path.expanduser(self.result_path)):
            pass
        else:
            os.system("mkdir " + self.result_path)

        if self.debug_mode:
            print("the result will be store at the path: ", self.result_path)

        # clone the repo
        self.gitClone()

        return

    """
    return the current working repo path
    """

    def getRepoDir(self) -> str:
        if self.debug_mode:
            print("current working dir: " + self.repo_path + "\n")
        return self.repo_path

    """
    find all .py file in the current working repo 
    """

    def findAllPyFile(self) -> list:
        all_files = []

        # find all files end up with .py
        for root, ds, fs in os.walk(self.repo_path):
            for f in fs:
                if f.endswith(".py"):
                    fullname = os.path.join(root, f)
                    all_files.append(fullname)

        # too many to print, decomment to see if want
        if self.debug_mode:
            print("Found the total python files: ", len(all_files), "\n")

        return all_files

    """
    check out to the corresponding commit 
    """

    def gitCheckOut(self, commit_id) -> None:

        if self.debug_mode:
            sys.stderr.write("checking out to commid: " + str(commit_id) + "\n")

        os.system(
            "cd "
            + self.repo_path
            + "/"
            + self.repo_name
            + " && git checkout "
            + commit_id
        )
        sleep(1)
        return

    """
    clone the repo
    """

    def gitClone(self) -> None:
        # check if the package exsits:
        if os.path.exists(self.repo_path):
            if self.debug_mode:
                print("current package: ", self.repo_name, " is already downloaded")
            return
        else:
            os.system("git clone --recursive " + self.download_link)
            return

    """
    read the file
    """

    def load_file(self, path) -> str:
        file = open(path, "r")
        content = file.read()
        file.close()
        return content

    """
    store the apis to the output json file 
    """

    def store_apis(self, added_apis, removed_apis, param_apis, return_apis, depre_apis):
        # udner the corresponding package
        file_name = self.repo_name + ".json"
        file_path = os.path.join(self.result_path, file_name)

        # clean the existed one
        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "w") as json_file:
            json.dump(
                {
                    "Added:": added_apis,
                    "Removed": removed_apis,
                    "Param_Changed": param_apis,
                    "Return_Changed": return_apis,
                    "Deprecated": depre_apis,
                },
                json_file,
                indent=4,
            )
        return

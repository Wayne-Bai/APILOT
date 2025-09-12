from github import Github, RateLimitExceededException
from datetime import datetime, timedelta
import json
import os
import sys
import time
import calendar
import pickle


"""
 Module: Preprocessor
 Function: Based on the commit dates, searching for the corresponding commit id cloest to that date 
"""


class Preprocessor:
    def __init__(self, owner, name, DEBUG) -> None:
        self.access_token = "YOUR GITHUB ACCESS TOKEN"
        self.owner = owner
        self.repo_name = name
        self.debug_mode = DEBUG

    """
    get the git repo 
    """

    def get_repo(self) -> object:

        flag = True
        while flag:
            try:
                g = Github(self.access_token)
                repo = g.get_repo(f"{self.owner}/{self.repo_name}")
                flag = False
            except RateLimitExceededException:
                g_temp = Github()
                search_rate_limit = g_temp.get_rate_limit().search
                print(
                    "The ramaining search rate limit is: {}".format(
                        search_rate_limit.remaining
                    )
                )
                reset_timestamp = calendar.timegm(search_rate_limit.reset.timetuple())
                sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 10
                print(
                    "The remaining waiting time should be: {} seconds".format(
                        sleep_time
                    )
                )
                time.sleep(sleep_time)

        return repo

    """
    get a commit sha closest to the commit date 
    dump the result to the map binary for using next time 
    """

    def getCommitId(self, date) -> object:
        repo = self.get_repo()
        # Get commits
        commits = repo.get_commits()

        # Convert date string to datetime object
        target_date = date

        # Find the closest commit to the target date
        closest_commit = None
        closest_diff = timedelta.max

        if self.debug_mode:
            print("searching for the commid Id cloest to the date: ", target_date)

        # current python script dir and file path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "map.pkl")

        # load the pickle map
        commit_map = {}
        with open(file_path, "rb") as f:
            file_size = os.path.getsize(file_path)
            if file_size != 0:
                commit_map = pickle.load(f)

        # search from the map first
        search_key = (self.repo_name, date)
        if search_key in commit_map:
            if self.debug_mode:
                print("Found the commid Id in the Map: ", commit_map[search_key])
            return commit_map[search_key]

        if self.debug_mode:
            print("searching from the total commits count: ", commits.totalCount)

        # search all the commits
        for commit in commits:
            commit_date = commit.commit.author.date
            diff = abs(commit_date - target_date)
            if diff < closest_diff:
                closest_diff = diff
                closest_commit = commit

        if closest_commit:
            if self.debug_mode:
                print("Finding the commid Id: ", closest_commit.sha)

            # write to the map
            commit_map[search_key] = closest_commit.sha

            # dump to the file
            with open(file_path, "wb") as f:
                pickle.dump(commit_map, f)

            return closest_commit.sha
        else:
            sys.stderr.write("no Found Commid ID for: " + target_date)
            return None

""" Class to manage crawls"""
from typing import List, final
from configparser import ConfigParser
from pathlib import Path

# Local modules
from searcher import Searcher

# Macros
MAX_STARTER_LINKS: final = 100 # Number of maximum starting links, assuming reading from a file

class Crawler:

    def __init__(self, domains: List[str], path: str):
        """ Add list to domains to crawl."""
        config = ConfigParser()

        ppath = Path(path)
        if not ppath.exists():
            raise FileNotFoundError(f"{path} does not exist in cwd")

        config.read(path)

        self.time = config["DEFAULT"].getfloat("time", 0)
        if self.time <= 0:
            raise Exception(f"time is currently set to {self.time}. Set > 0")

        self.result_file = config["STORAGE"].get("results", "")
        if self.result_file == "":
            raise Exception(f"Missing 'STORAGE' section or 'STORAGE/results' is empty/DNE")

        if len(domains):
            self.searcher = Searcher(domains)
        else:
            previousQueue = config["STORAGE"].get("YetToCrawl", "")
            if previousQueue == "":
                raise Exception(f"Missing 'STORAGE/results'")
            elif not Path(previousQueue).exists():
                raise Exception(f"Path {previousQueue} does not exist")

            toSearch = []
            with open(previousQueue, "r") as f:
                i = 0
                for line in f:
                    toSearch.append(line)

            with open(previousQueue, "w") as f: # Clear file
                pass

            self.searcher = Searcher(toSearch)
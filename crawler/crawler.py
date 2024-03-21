""" Class to manage crawls"""
from typing import List
from configparser import ConfigParser
from pathlib import Path

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

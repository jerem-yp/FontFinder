""" Implements a BFS Searcher. """
from typing import List
import queue

class Searcher:

    def __init__(self, lst_domains: List[str]):
        # Set up the queue for BFS
        self.links = queue.Queue(maxsize = 0) # Infinite Size
        for item in lst_domains:
            self.links.put(item)

    def getNext(self) -> str:
        """ Get the next item. Returns empty string if none"""
        return "" if self.links.empty() else self.links.get()

    def add(self, link: str) -> None:
        """ Add an item to this searcher."""
        self.links.put(link)
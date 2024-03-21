import sys
import os
from typing import List, Tuple

# Local modules
from crawler import Crawler

PATH = os.path.join(".", "init", "rules.ini")
def main():
    # Starts the crawler, using cmdline
    simpleCrawler = Crawler(sys.argv[1:], PATH)

if __name__ == "__main__":
    main()
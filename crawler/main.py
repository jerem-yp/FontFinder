import sys
from typing import List, Tuple

# Local modules
from crawler import Crawler

def main():
    # Starts the crawler, using cmdline
    simpleCrawler = Crawler(sys.argv[1:])

if __name__ == "__main__":
    main()
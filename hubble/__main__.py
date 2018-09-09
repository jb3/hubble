#!/usr/bin/env python3

"""
Hubble search tool for GitHub
"""

import argparse
import sys

import colorama

from search import search
from display import display

__author__ = "Joseph Banks"
__copyright__ = "Copyright 2018, Joseph Banks"
__credits__ = ["Joseph Banks"]

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Joseph Banks"
__email__ = "joseph@josephbanks.me"

if __name__ == "__main__":
    colorama.init()

    parser = argparse.ArgumentParser(description="Search GitHub.")

    parser.add_argument("search_terms", metavar="search terms",
                        type=str, nargs='+',
                        help="The terms to search GitHub for.")

    parser.add_argument("--version", "-v", action="version",
                        version=f"{sys.argv[0]} {__version__}")

    parser.add_argument("--type", "-t", metavar="type", type=str,
                        default="repository",
                        choices=["repository", "user"],
                        help="The type of object to search"
                             "GitHub for. (Default: repository)")

    parser.add_argument("--limit", "-l", type=int,
                        default=10,
                        help="The number of results to "
                             "display. (Default: 10)")

    args = parser.parse_args()

    github_response, search_type = search(args)

    try:
        display(github_response, search_type)
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

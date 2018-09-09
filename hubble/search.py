"""
Module to interface with the GitHub Search API.
"""

import argparse
import enum
import sys
import typing

import requests

__author__ = "Joseph Banks"

GITHUB_API_BASE = "https://api.github.com"


class SearchType(enum.Enum):
    """
    This Enum represents the types of searches we can perform
    """
    REPOSITORIES = "repositories"
    COMMITS = "commits"
    CODE = "code"
    ISSUES = "issues"
    USERS = "users"
    TOPICS = "topics"


def search(args: argparse.Namespace) -> typing.Tuple[dict, SearchType]:
    """
    This function takes in our argparse namespace and converts it into 2
    useful variables, endpoint + search_type.

    endpoint will be used in the next function where we will need to use
    a specific route on the GitHub API to achieve the right query.

    We use search_type both in the next function and back in the results
    display functions so that we know how we should format our results.
    """
    if args.type == "repository":
        endpoint = "/search/repositories"
        search_type = SearchType.REPOSITORIES
    elif args.type == "commit":
        endpoint = "/search/commits"
        search_type = SearchType.COMMITS
    elif args.type == "code":
        endpoint = "/search/code"
        search_type = SearchType.CODE
    elif args.type == "issue":
        endpoint = "/search/issues"
        search_type = SearchType.ISSUES
    elif args.type == "user":
        endpoint = "/search/users"
        search_type = SearchType.USERS
    elif args.type == "topic":
        endpoint = "/search/topic"
        search_type = SearchType.TOPICS
    else:
        raise Exception("Invalid type error, this should never happen."
                        "Please report it at "
                        "https://github.com/jos-b/hubble/issues")

    endpoint = GITHUB_API_BASE + endpoint

    return search_with_type(endpoint, search_type, args), search_type


def search_with_type(endpoint: str,
                     search_type: SearchType,
                     args: argparse.Namespace) -> dict:
    """
    Perform search, we get an endpoint, a search_type and the args.

    We simply join the users input and send the request to the
    GitHub API.

    We quickly perform some checks to make sure we don't have no results,
    if we don't we return the response.
    """
    req = requests.get(endpoint, params={"q": " ".join(args.search_terms)})

    resp = req.json()

    if len(resp["items"]) == 0:
        print("No results found")
        sys.exit(0)

    items = req.json()["items"]

    items = items[0:args.limit]

    return items

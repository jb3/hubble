"""
This module is used to display the results from the
GitHub API in a nice way.
"""

from .search import SearchType

from colorama import Fore, Style

__author__ = "Joseph Banks"


def reset(text: str) -> str:
    return text + Style.RESET_ALL


def display(results: dict, search_type: SearchType):
    if search_type == SearchType.REPOSITORIES:
        display_repos(results)
    elif search_type == SearchType.USERS:
        display_users(results)


def display_users(results: dict):
    for number, item in enumerate(results):
        print(reset(f"{Fore.LIGHTMAGENTA_EX}{number + 1}."
                    f" {Style.BRIGHT}{Fore.LIGHTGREEN_EX}"
                    f"{item['login']}"))

    number = input(reset(f"{Fore.LIGHTGREEN_EX}Enter number for"
                         f" more information\n=> "))

    try:
        number = int(number)
    except ValueError:
        print(reset(f"{Fore.RED}Invalid number!"))
        display_users(results)
        return

    if number < 1 or number > len(results):
        print(reset(f"{Fore.RED}Invalid number!"))
        display_users(results)
        return

    user = results[number - 1]

    RA = Style.RESET_ALL

    print(reset(f"{Fore.LIGHTGREEN_EX}{user['login']}{RA}"
                f"\n\t{Style.DIM}ID: {RA}{user['id']}"
                f"\n\t{Style.DIM}Web URL: {RA}{user['html_url']}"))


def display_repos(results: dict):
    for number, item in enumerate(results):
        print(reset(f"{Fore.LIGHTMAGENTA_EX}{number + 1}."
                    f" {Style.BRIGHT}{Fore.LIGHTGREEN_EX}"
                    f"{item['owner']['login']}{Style.RESET_ALL}"
                    f"/{Style.BRIGHT}{item['name']}"
                    f"\n\t{Style.DIM}{item['description']}"))

    number = input(reset(f"{Fore.LIGHTGREEN_EX}Enter number for"
                         f" more information\n=> "))

    try:
        number = int(number)
    except ValueError:
        print(reset(f"{Fore.RED}Invalid number!"))
        display_repos(results)
        return

    if number > len(results) or number < 1:
        print(reset(f"{Fore.RED}Invalid number!"))
        display_repos(results)
        return

    repo = results[number - 1]

    RA = Style.RESET_ALL

    print(reset(f"{Fore.LIGHTGREEN_EX}{repo['full_name']}"
                f"\n\t{Style.DIM}{repo['description']}{RA}"
                f"\n\n\t{Style.DIM}Watchers: {RA}{repo['watchers_count']}"
                f"\n\t{Style.DIM}Stars: {RA}{repo['stargazers_count']}"
                f"\n\t{Style.DIM}Forks: {RA}{repo['forks_count']}"
                f"\n\t{Style.DIM}Language: {RA}{repo['language']}"
                f"\n\t{Style.DIM}Web URL: {RA}{repo['html_url']}"
                f"\n\t{Style.DIM}Git URL: {RA}{repo['git_url']}"
                f"\n\t{Style.DIM}SSH URL: {RA}{repo['ssh_url']}"))

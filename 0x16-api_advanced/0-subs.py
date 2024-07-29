#!/usr/bin/python3
"""This module queries the Reddit API and returns the number of subscribers"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python/requests"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-main.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        print(f"Number of subscribers in subreddit '{subreddit}': {number_of_subscribers(subreddit)}")

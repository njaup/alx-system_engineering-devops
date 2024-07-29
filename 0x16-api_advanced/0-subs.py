#!/usr/bin/python3
"""This module queries Reddit API and returns the number of subscribers"""

import json
import requests

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my-custom-user-agent-v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

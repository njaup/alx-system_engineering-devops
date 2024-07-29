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
        print(f"HTTP Status Code: {response.status_code}")  # Debugging output
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response JSON: {data}")  # Debugging output
            return data['data']['subscribers']
        else:
            print(f"Unexpected status code: {response.status_code}")  # Debugging output
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit does not exist or there is an error, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": (
            "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"
        )
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        pass

    return 0

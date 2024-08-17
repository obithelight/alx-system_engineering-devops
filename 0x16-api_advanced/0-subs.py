#!/usr/bin/python3
"""Queries the `Reddit API`, returns the number of subscribers
    of a subreddit
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code == 200:
        subscribers = data.json().get("data").get("subscribers")
        return subscribers
    return 0

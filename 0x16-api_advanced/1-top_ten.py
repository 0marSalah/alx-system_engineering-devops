#!/usr/bin/python3
""" top 10 hot posts """
import requests


def top_ten(subreddit):
    """
    query top 10 hot posts
    Args:
        subreddit: name of the subreddit
    """
    url = f"https://reddit.com/r/{subreddit}/top.json"
    header = {'User-Agent': "Mozilla/5.0"}
    params = {'limit': 10}
    response = requests.get(url, headers=header, params=params)

    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    for post in data.get("data", {}).get("children", []):
        print(post.get("data", {}).get("title", ""))

#!/usr/bin/python3
""" Recursively query Reddit API """


import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Return Reddit hot list recursively """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after}
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list

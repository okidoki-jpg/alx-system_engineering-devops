#!/usr/bin/python3
""" Querries to Reddit API """


import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    return 0

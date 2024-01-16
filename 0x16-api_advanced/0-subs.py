#!/usr/bin/python3
""" Querries to Reddit API """


import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0)\
    Gecko/20100101 Firefox/110.0.'}
    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        r.raise_for_status()
        return r.json()['data']['subscribers']
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
    except KeyError:
        return 0

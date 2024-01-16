#!/usr/bin/python3
""" count hot article keywords """


import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """ count words """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            title = child.get('data').get('title')
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        if after:
            return count_words(subreddit, word_list, after, word_dict)
        else:
            if not len(word_dict) > 1:
                return
            for key, value in sorted(word_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                print(f'{key}: {value}')

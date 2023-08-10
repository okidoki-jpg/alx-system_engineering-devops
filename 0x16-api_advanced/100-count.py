#!/usr/bin/python3
""" count hot article keywords """


def count_words(subreddit, word_list, after=None, word_dict={}):
    """ count words """
    import requests
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton Project)'}
    params = {'after': after}
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        after = r.json().get('data').get('after')
        children = r.json().get('data').get('children')
        for child in children:
            title = child.get('data').get('title')
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        if after is not None:
            return count_words(subreddit, word_list, after, word_dict)
        else:
            if len(word_dict) == 0:
                return
            else:
                for key, value in sorted(word_dict.items(),
                            key=lambda item: item[1],
                            reverse=True):
                    print(f'{key.lower()}: {value}')
    else:
        return

#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers'''

import requests


def number_of_subscribers(subreddit):
    """Function that returns subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/70.0.3538.77 Safari/537.36'}
    r = requests.get(url.format(subreddit), headers=headers).json()
    subs = r.get('data', {}).get('subscribers', 0)
    return subs

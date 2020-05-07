#!/usr/bin/python3
'''Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.'''

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit."""
    if after is None:
        return []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/70.0.3538.77 Safari/537.36'}
    if after:
        url += '?after={}'.format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if str(r) != '<Response [200]>':
        return None
    rjson = r.json()
    hotPosts = rjson.get('data').get('children')
    for post in hotPosts:
        hot_list.append(post.get('data').get('title'))
    return hot_list + recurse(subreddit, [], rjson.get('data').get('after'))

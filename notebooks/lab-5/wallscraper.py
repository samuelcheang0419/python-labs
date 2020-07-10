#!/usr/bin/env python3
"""
Reddit Wallscraper
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
import wallscraperutils
import requests
import datetime


class RedditPost:
    def __init__(self, data):
        keep_keys = ['subreddit', 'ups', 'post_hint', 'title', 'downs', 'score', 'url', 'domain', 'permalink', 'created_utc', 'num_comments', 'preview', 'name', 'over_18']
        self.data = dict((k, data.get(k, None)) for k in keep_keys)

    def has_image(self):
        # check object has downloadable image: 
        # Is the post_hint attribute image, link, or something else? 
        if self.data['post_hint'] == 'image':
            return True
        # You can look at the url - does it end with '.jpg','.png'. or any other image suffix? 
        # Is the domain something recognizable like 'i.imgur.com'?
        in_url = ['.jpg', '.png', 'imgur.com']
        if any(s in self.data['url'] for s in in_url):
            return True
        return False

    def download(self):
        if self.has_image():
            filename = 'test'
            with open(filename, 'wb') as f:
                f.write(requests.get(self.data['url']).content)
                print('Downloaded image at {} as filename {}'.format(self.data['url'], filename))
        else:
            print('No downloadable image')
        return

    def __str__(self):
        return "RedditPost({} ({}): {})".format(self.data['title'], self.data['score'], self.data['url'])

    
def query(subreddit):
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    try:
        headers = {'User-Agent': 'Wallscraper script'}
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Trying GET request from url = {}\non {}..'.format(url, now))
        response = requests.get(url, headers = headers)
    except Exception as exc:
        print('Python request module threw exception')
        print(type(exc))
        print(exc.args)
    if not response.ok:
        print('Request response not ok (response.ok = false)')
        print('{}: {}'.format(response.status_code, response.reason))
        return
    else:
        response_json = response.json()
        if response_json['data']['dist'] == 0:
            print('Subreddit does not exist/no posts')
            return
        return response_json
    
    
def main():
    children = query('wallpapers')['data']['children']
    things = [RedditPost(thing['data']) for thing in children]
    return things


if __name__ == '__main__':
    main()

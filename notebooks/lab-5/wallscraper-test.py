import wallscraperutils
import requests
import datetime
import wallscraper

def query_test():
    '''
    Query a reasonable subreddit and compute the number of posts with a score 
    greater than 500 using the `query` function
    '''
    subreddit = 'wallpapers'
    json = wallscraper.query(subreddit)
    print('Number of posts with a score greater than 500: {}'.format(
        len(list(filter(lambda x: x['data']['score'] > 500, json['data']['children']))))
    )


def main_test():
    '''
    Same as query_test() but calling main() instead
    '''
    posts = wallscraper.main()
    print('Number of posts: {}'.format(len(posts)))
    print('Number of posts with a score greater than 500: {}'.format(
        len(list(filter(lambda x: x.data['score'] > 500, posts))))
    )


def RedditPost_test():
    posts = wallscraper.main()
    redditpost = posts[0]
    print(redditpost)
    redditpost.download()


if __name__ == '__main__':
    # query_test()
    # main_test()
    RedditPost_test()

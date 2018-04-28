# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter import *
from spec_char_remover import remove_spec
import time
from urllib.request import urlopen

def set_twitter_api(): 

    consumer_key = 'lkNdx5veeHfkGddtdnmvcej2z'
    consumer_secret = 'DJ7UzhKJAocdOOhwLOEB9OpjEgwgwOeJZstjm8RERLYa6sSNWi'
    access_key = '3874598667-VFtiu01zBsy7UZMFSZLM6iZNbztW6K6cAyliR5j'
    access_secret = 'oNzEwXqRC91tRDJccl5fH6CxkqJoAlKthNLRwlBHjVAGT'
    api = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
    return api
        
def twitter_search_team(team_name):
    # create twitter API object
    twitter = set_twitter_api()
    team_name = remove_spec(team_name)
    search_result = twitter.users.search(q = '"' + team_name + '"')
    try:
        tweets = twitter.statuses.user_timeline(screen_name = team_name, count=200)
        favs = 0
        retweets = 0
        cnt = 0
        hashtags = []
        for tweet in tweets:
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
        hashtags = list(set(hashtags))
        hashtags = " ".join(str(x) for x in hashtags)
        for tweet in tweets:
            if tweet['favorite_count'] != 0:
                favs += tweet['favorite_count']
                retweets += tweet['retweet_count']
                cnt += 1
            if cnt == 10:
                break
        avg_fav = int(round(favs/ 10))
        avg_retweet = int(round(retweets / 10))
    except:
        avg_fav = "NaN"
        avg_retweet = "NaN"
        hashtags = "No hashtags found"
    if len(search_result) > 0:
        user = search_result[0]
        # Expand the urls
        try:
            tco_url = user["url"]
            req = urlopen(tco_url)
            url = req.url
        except:
            url = "NaN"
        # Format the date into a correct form
        created_at = time.strftime('%Y-%m-%d', time.strptime(user["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))
        page_dict = {'twitter_name' : user["screen_name"],
                     'twitter_loc' : user["location"],
                     'twitter_id' : user["id"],
                     'twitter_followers' : user["followers_count"],
                     'twitter_friends' : user["friends_count"],
                     'twitter_favs_count' : user["favourites_count"],
                     'twitter_created_at' : created_at,
                     'twitter_statuses' : user["statuses_count"],
                     'twitter_avg_fav' : avg_fav,
                     'twitter_avg_retweet': avg_retweet,
                     'twitter_url' : url,
                     'twitter_hashtags' : hashtags
                     }
        return page_dict
    else:
        page_dict = {'twitter_name' : "NaN",
                     'twitter_loc' : "NaN",
                     'twitter_id' : "NaN",
                     'twitter_followers' : "NaN",
                     'twitter_friends' : "NaN",
                     'twitter_favs_count' : "Nan",
                     'twitter_created_at' : "NaN",
                     'twitter_statuses' : "NaN",
                     'twitter_avg_fav' : "NaN",
                     'twitter_avg_retweet': "NaN",
                     'twitter_url' : "NaN",
                     'twitter_hashtags' : "NaN"
                     }
        return page_dict

def generate_twitter_csv(team_list):
    raise NotImplementedError
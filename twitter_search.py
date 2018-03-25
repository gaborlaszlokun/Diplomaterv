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
                     'twitter_id' : user["id"],
                     'twitter_followers' : user["followers_count"],
                     'twitter_created_at' : created_at,
                     'twitter_statuses' : user["statuses_count"],
                     'twitter_url' : url
                     }
        return page_dict
    else:
        page_dict = {'twitter_name' : "NaN",
                     'twitter_id' : "NaN",
                     'twitter_followers' : "NaN",
                     'twitter_created_at' : "NaN",
                     'twitter_statuses' : "NaN",
                     'twitter_url' : "NaN"
                     }
        return page_dict

def generate_twitter_csv(team_list):
    raise NotImplementedError
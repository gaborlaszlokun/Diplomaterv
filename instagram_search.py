# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:03:29 2018

@author: ASUS
"""

import pandas as pd
from bs4 import BeautifulSoup
import urllib
import json

def instagram_search_team(query):
    
    url = "https://www.instagram.com/" + query
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    data= con.read()
    soup = BeautifulSoup(data, 'html.parser')
    insta_json = soup.findAll('script', { "type" : "text/javascript" })
    insta_json = insta_json[2].getText().replace("window._sharedData = ","")[:-1]
    
    
    insta_json = json.loads(insta_json)
    hashtags = str(insta_json).translate(str.maketrans('','', ",'\\\"!.;{}[]")).split(" ")
    hashtags = set([x for x in hashtags if x.startswith("#")])
                                              
    #print(hashtags)
    
    root = insta_json['entry_data']['ProfilePage'][0]['graphql']['user']
    #print(root["profile_pic_url_hd"])

    # i alapján az utolsó 10 content adatai
    i = 0
    last_like = root['edge_owner_to_timeline_media']['edges'][i]['node']['edge_liked_by']['count']
    last_comment = root['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_comment']['count']
    last_img_url = root['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']

    print(last_like, last_comment, last_img_url)
    page_dict = {'instagram_name' : root['username'],
                 'instagram_id': root['id'],
                 'instagram_media': root['edge_owner_to_timeline_media']['count'],
                 'instagram_followers': root['edge_followed_by']['count'],
                 'instagram_follows' : root['edge_follow']['count'],
                 'instagram_url' : root["external_url"]}
    return page_dict

"""
team_name = "udinesecalcio"
for key, value in instagram_search_team(team_name).items():
    print (key, ":", value)
    
"""
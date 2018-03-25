# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from instagram_search import *

team = "gzs10.05"

for key, value in instagram_search_team(team).items():
    print (key, ":", value)
 
#print (get_instagram_name(team))
#print (get_instagram_id(team))
#print (get_instagram_media(team))
#print (get_instagram_followers(team))
#print (get_instagram_follows(team))
#print (get_instagram_url(team))
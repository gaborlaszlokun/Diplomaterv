# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter_search import *

team_name = "manutd"

for key, value in twitter_search_team(team_name).items():
    print (key, ":", value)

#team_dict = twitter_search_team(team_name)
#print team_dict
#    
#print get_twitter_name(team_name)
#print get_twitter_id(team_name)
#print get_twitter_followers(team_name)
#print get_twitter_created_at(team_name)
#print get_twitter_statuses(team_name)
#print get_twitter_url(team_name)
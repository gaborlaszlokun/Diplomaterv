# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *
from instagram_search import *
from twitter_search import *

def social_media_search(team_alts):
    if len(team_alts) == 3:
        team_dict = facebook_search_team(team_alts[0])
        team_dict.update(twitter_search_team(team_alts[1]))
        team_dict.update(instagram_search_team(team_alts[2]))
    else:
        team_dict = facebook_search_team(team_alts)
        team_dict.update(twitter_search_team(team_alts))
        team_dict.update(instagram_search_team(team_alts)) 

    return team_dict
    
def print_result(team):
#    print (social_media_search(team))
    for key, value in social_media_search(team).items():
        print (key, ":", value)
    
def save_main_teams(team):
    raise NotImplementedError

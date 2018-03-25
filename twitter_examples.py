# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter_search import *

team_name = "manutd"

for key, value in twitter_search_team(team_name).items():
    print (key, ":", value)
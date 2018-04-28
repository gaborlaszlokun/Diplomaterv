# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:00:44 2018

@author: ASUS
"""

import pandas as pd
from social_media_search import  *

teams = pd.read_csv("main_teams.csv")

teams = teams[["query","facebook_id", "twitter_name", "instagram_name"]]
print(teams)
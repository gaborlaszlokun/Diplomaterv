# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from instagram_search import *

team = "olympiquedemarseille"

for key, value in instagram_search_team(team).items():
    print (key, ":", value)
 
#print (instagram_search_team(team)['instagram_hashtags'][0])
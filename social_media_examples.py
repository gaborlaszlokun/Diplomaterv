# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from social_media_search import  *

team = ["302193069794158","RealSociedadEN","realsociedad"]

for key, value in social_media_search(team).items():
    print (key, ":", value)

#social_media_search(team)['instagram_name']
#social_media_search(team)['instagram_id']
   
#print_result(team)
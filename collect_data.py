# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:44:53 2018

@author: ASUS
"""

import pandas as pd
from social_media_search import  *

teams = pd.read_csv("main_teams.csv")

teams = teams[["query","facebook_id", "twitter_name", "instagram_name"]]

def generate_basic_csv():
    columns = ['team',
               'facebook_name',
               'facebook_likes',
               'facebook_talking_about_count',
               'facebook_url',
               'twitter_name',
               'twitter_followers',
               'twitter_friends',
               'twitter_favs_count',
               'twitter_statuses',
               'twitter_url',
               'instagram_name',
               'instagram_profile_pic_url',
               'instagram_media',
               'instagram_followers',
               'instagram_follows',
               'instagram_url',
               'hashtags'
               ]

    result_df = pd.DataFrame(columns=columns)
    index = 0
    for index,row in teams.iterrows():
    #    print(social_media_search([str(row[0]),row[1],row[2]]))
        result = social_media_search([str(row[1]),row[2],row[3]])
        #print(row[0], result['twitter_loc'])
        hashtags = result['instagram_hashtags'] + " " + result['twitter_hashtags']

        result_line_df = pd.DataFrame([[row[0],
                                        result['facebook_name'],
                                        result['facebook_likes'],
                                        result['facebook_talking_about_count'],
                                        result['facebook_url'],
                                        result['twitter_name'],
                                        result['twitter_followers'],
                                        result['twitter_friends'],
                                        result['twitter_favs_count'],
                                        result['twitter_statuses'],
                                        result['twitter_url'],
                                        result['instagram_name'],
                                        result['instagram_profile_pic_url'],
                                        result['instagram_media'],
                                        result['instagram_followers'],
                                        result['instagram_follows'],
                                        result['instagram_url'],
                                        hashtags
                                        ]], columns=columns, index = [index])
        index += 1
        print(index)
        result_df = result_df.append(result_line_df)
    result_df.to_csv("teams_basic_data.csv",encoding='utf-8', index=False)

def generate_loc_csv():
    columns = ['team','city']
    result_df = pd.DataFrame(columns=columns)
    index = 0
    for index,row in teams.iterrows():
    #    print(social_media_search([str(row[0]),row[1],row[2]]))
        result = social_media_search([str(row[1]),row[2],row[3]])
        #print(row[0], result['twitter_loc'])
        
        result_line_df = pd.DataFrame([[row[0], result['twitter_loc']]], columns=columns, index = [index])
        index += 1
        result_df = result_df.append(result_line_df)
    result_df.to_csv("teams_with_locs.csv",encoding='utf-8', index=False)

#generate_basic_csv()  

 
loc = pd.read_csv("teams_with_locs.csv")
team_data = pd.read_csv("teams_basic_data.csv")
total = loc.merge(team_data)
total.to_csv("teams_data.csv",encoding='utf-8', index=False)

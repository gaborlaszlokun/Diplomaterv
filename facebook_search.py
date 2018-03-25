# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from urllib.request import urlopen, Request
import json
import pandas as pd
from django.utils.encoding import smart_str
from facebook_config import *
from spec_char_remover import remove_spec

access_token = get_facebook_access_token()

def get_page_from_id(page_id):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint + page_id + "?fields=id,rating_count,were_here_count,name,likes,link,talking_about_count,category&access_token=" + access_token
    try:
        api_request = Request(fb_graph_url)
        api_response = urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except (IOError):
        None

def facebook_search_team(team_id):
    try:
        page_json = get_page_from_id(team_id)
        page_dict = {'facebook_name' : page_json['name'].replace(",",";"),
                     'facebook_id' : page_json['id'],
                     'facebook_likes' : page_json['likes'],
                     'facebook_talking_about_count' : page_json['talking_about_count'],
                     'facebook_category' : page_json['category'].replace(",",";"),
                     'facebook_url' : page_json['link'].replace(",",";"),
                     'facebook_rating_count' : page_json['rating_count'],
                     'facebook_were_here_count' : page_json['were_here_count']
                     }
        return page_dict
    except:
        page_dict = {'facebook_name' : "NaN",
                     'facebook_id' : "NaN",
                     'facebook_likes' : "NaN",
                     'facebook_talking_about_count' : "NaN",
                     'facebook_category' : "NaN",
                     'facebook_url' : "NaN",
                     'facebook_rating_count' : "NaN",
                     'facebook_were_here_count' : "Nan"
                     }
        return page_dict

def get_facebook_page_fans(query,access_token, start_date, final_date):
    fb_graph_url = "https://graph.facebook.com/v2.6/" + query + "/insights/page_fans_country/lifetime?&since=" + start_date + "&until=" + final_date + "&access_token=" + access_token
    
    
    try:
        api_request = Request(fb_graph_url)
        api_response = urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except (IOError):
        None

 
#TODO: refactor
def generate_facebook_csv(team_list):
    output_name = team_list.replace("list","facebook_stats")
    csv_header = "facebook_name,facebook_id,facebook_likes,facebook_talking_about_count,facebook_category,facebook_url\n"
    result_csv = open(output_name, "a")
    result_csv.write(csv_header)
    result_csv.close()
    teams = pd.read_csv(team_list)
    for i in range(len(teams)):
        team_name = teams.iat[i,0]
        print (team_name)
        team_stats = facebook_search_team(team_name)
        result_line = ""
        result_line += team_stats['facebook_name'] + ","
        result_line += str(team_stats['facebook_id']) + ","
        result_line += str(team_stats['facebook_likes']) + ","
        result_line += str(team_stats['facebook_talking_about_count']) + ","
        result_line += team_stats['facebook_category']
        result_line += "," + team_stats['facebook_url']
        result_line += "\n"
        result_line = smart_str(result_line)
        print (result_line)
        
        result_csv = open(output_name, "a")
        result_csv.write(result_line)
        result_csv.close()

"""
Some extra links

link = "https://graph.facebook.com/DiamondPlatnumz255?access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648"
https://graph.facebook.com/v2.6/204153042939851/posts/?fields=message,link,permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)&limit=100&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
https://graph.facebook.com/search?q=manchester+united&type=page&access_token=614700401966588%7C7af8b0fda1b43f908b8853ed65e8b648
https://graph.facebook.com/v2.6/barackobama/insights/page_fans_country/lifetime?&since=2016-06-01&until=2016-09-02&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
https://graph.facebook.com/v2.6/7724542745/insights/page_fans_country/lifetime?&since=2016-06-01&until=2016-09-02&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648

"""
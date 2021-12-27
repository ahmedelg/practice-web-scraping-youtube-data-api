from os import P_DETACH
from googleapiclient.discovery import build
import pandas as pnd

import csv
import seaborn


# youtube_api_key = 'AIzaSyDPVy2nL_Y1KhVFjeasUAs_opDZWDxLxWU'
youtube_api_key = 'AIzaSyBrApnUY0EeTmxMAybd51x3lKGKGsdqtCg'

# channel_id = 'UCnz-ZXXER4jOvuED5trXfEA'
# channel_id = 'UCnz-ZXXER4jOvuED5trXfEA'

channel_ids=['UCnz-ZXXER4jOvuED5trXfEA','UCBO_EiHRQQnYsclHIjUJUJQ','UCW5YeuERMmlnqo4oq8vwUpg','UCFbNIlppjAuEX4znoulh0Cw','UCqeTj_QAnNlmt7FwzNwHZnA','UCqrILQNl5Ed9Dz6CGMyvMTQ',
             'UCSSr5ZDFbilpZ592_ycoAwA']

api_service_name = 'youtube'
api_version = "v3"

youtube = build(api_service_name, api_version, developerKey=youtube_api_key)

# print(type(youtube))
# <class 'googleapiclient.discovery.Resource'>



def extract_channel_data(channel_data_res):
  items = channel_data_res['items'][0]
  snippet = items['snippet']
  statistics = items['statistics']
  # channel_data = dict(
  #     channel_id=items['id'],
  #     channel_name=snippet['title'],
  #     channel_desc=snippet['description'],
  #     channel_published=snippet['publishedAt'],
  #     channel_thumbnail=snippet['thumbnails']['default']['url'],
  #     channel_country=snippet['country'],
  #     channel_statistics={
  #       'views_count':statistics['viewCount'],
  #       'subscribers_count':statistics['subscriberCount'],
  #       'hidden_subscribe_count':statistics['hiddenSubscriberCount'],
  #       'video_count':statistics['videoCount']
  #     }
  # )
  # return channel_data
  
  try:
    channel_extracted_data=[
      snippet['title'],
      items['id'],
      snippet['description'],
      snippet['publishedAt'],
      snippet['thumbnails']['default']['url'],
      snippet['country'],
      statistics['viewCount'],
      statistics['subscriberCount'],
      statistics['hiddenSubscriberCount'],
      statistics['videoCount']
    ]
  except AttributeError:
    channel_extracted_data=[]
  except KeyError:
    channel_extracted_data=[] 
  return channel_extracted_data


# SAVE FILE WITH CHANNELS EXTRACTED DATA
def save_channel_data(channel_extracted_data):
  with open ('youtube_channels_data.csv','a', newline='',encoding='utf-8') as csv_file:
    csv_writer=csv.writer(csv_file,delimiter=',')
    csv_writer.writerow(channel_extracted_data)
    print('channel data has been stored.')

def fetch_channel_info(youtube, channel_ids):
  channels_data=[]
  # req = youtube.channels().list(
  #       part='snippet,contentDetails,statistics',
  #       id=','.join(channel_ids)
  # )
  # res = req.execute()
  # return res
  
  for channel_id in channel_ids:
    print('start channel id: '+channel_id)
    req = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_id
    )
    res = req.execute()
    # EXTRACT CHANNEL DATA
    print('extract channel:')
    channel_extracted_data=extract_channel_data(res)
    # return 'statistics'
    channels_data.append(channel_extracted_data)
    # SAVE CHANNEL EXTRACTED DATA IN CSV FILE
    save_channel_data(channel_extracted_data)
  # RETURN CHANNELS DATA
  return channels_data


channels_extracted_data = fetch_channel_info(youtube, channel_ids)

# print(channels_extracted_data)


  
  

# channels_extracted_data_table=pnd.DataFrame(channels_extracted_data)

# print(channels_extracted_data_table)


# print(len(channel_data_res['items']))




# print(channel_data)

# print(type(fetch_channel_info(youtube,channel_id)))

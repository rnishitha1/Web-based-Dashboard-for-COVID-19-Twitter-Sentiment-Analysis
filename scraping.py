# -*- coding: utf-8 -*-
"""Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18PPYA9gRnzeqt37LP6cxKO5lP8bWkl5N
"""

!pip install GetOldTweets3

import numpy as np
import pandas as pd
import GetOldTweets3 as got
import datetime
import os
from tqdm import tqdm

path = "/content/drive/My Drive/Covid19Data/"

for i in tqdm(range(1, 32)):
  dt = datetime.datetime(2020,5,i)
  dt_end = dt + datetime.timedelta(days=1)
  tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#lockdownindia OR #indialockdown OR #coronavirusindia OR #coronavirusinindia OR #coronaindia OR #covid19india OR #covid_19india OR #covid2019india OR #covidindia OR #indiafightscorona OR #indiafightscovid19 OR #indiafightscovid2019 OR #indiafightscovid OR #lockdown21 OR #indialockdown2 OR #indialockdown3 OR #indialockdown4 OR #indiaunlock OR #unlockindia OR #lockdownextensionindia OR #lockdowneffect')\
                                            .setSince(dt.strftime("%Y-%m-%d"))\
                                            .setUntil(dt_end.strftime("%Y-%m-%d"))\
                                            .setLang('en')\
                                            .setEmoji('unicode')\
                                            .setMaxTweets(500)
  tweet = got.manager.TweetManager.getTweets(tweetCriteria)
  text_tweets = [[tw.username,
                  tw.text,
                  tw.date,
                  tw.retweets,
                  tw.favorites,
                  tw.mentions,
                  tw.hashtags] for tw in tweet]
      
  news_df = pd.DataFrame(text_tweets, 
                              columns = ['user', 'text','date','favorites', 'retweets', 'mentions', 'hashtags'])
  news_df.to_csv(path + dt.strftime("%Y-%m-%d") + '.csv', index=False)

files = os.listdir(path)
combined_csv = pd.concat([pd.read_csv(path + f) for f in files ])
combined_csv.to_csv(path+'May.csv', index = False)
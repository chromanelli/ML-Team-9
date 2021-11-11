import pandas as pd
from pandas import DataFrame
from textblob import TextBlob

'''
This file aims to analyze the tweet data located in tweets.csv
'''

def remove_tagged(tweet_string):
    marker = False
    removal_list = []
    tmp = ''
    for i in range(len(tweet_string)):
        if tweet_string[i] == '@':
            marker = True
        if marker == True and tweet_string[i] != ' ':
            tmp = tmp + tweet_string[i]
        if marker == True and tweet_string[i] == ' ':
            removal_list.append(tmp)
            tmp = ''
            marker = False
    

    #print(tweet)
    #print(removal_list)
    for i in range(len(removal_list)):
        tweet_string = tweet_string.replace(removal_list[i], '')

    return tweet_string

if __name__ == "__main__":

    #Reading in tweet data csv
    df = pd.read_csv ('tweets.csv')

    #Iterating through data to find sentiment of tweet text
    sentiment_list = []
    for i in range(len(df)):


        tweet = str(df['text'].iloc[i])
        tweet = remove_tagged(tweet)
        testimonial = TextBlob(tweet)
        sentiment_list.append(testimonial.sentiment.polarity)

    #Storing sentiment onto new data frame column
    df['sentiment'] = sentiment_list
    outfile = DataFrame(df,columns=["id","created_at","favorite_count","retweet_count","text","sentiment"])
    df.to_csv('with_sentiment.csv',index=False)

import sys
import json
import error
import arg_dict
import preprocess
import os
import re
#Error handling
if error.check_cmd(len(sys.argv)) == True:
    sentimentData = sys.argv[1] 
    twitterData = sys.argv[2] 
else:
    sys.exit(-1)

#decode tweets in utf-8 format    
def tweet_dict(twitterData):  
    
    twitter_list_dict = []
    twitterfile = open(twitterData)
    for line in twitterfile:
        twitter_list_dict.append(json.loads(line.decode('utf-8-sig')))

    twitterfile.close()
    return twitter_list_dict

def main():

    tweets = tweet_dict(twitterData)#contains tweets
    sentiment = arg_dict.sentiment_dict(sentimentData)#contains dictionary of scores
    space=['']
    for index in range(len(tweets)):

        tweet_word = tweets[index]["text"].split() #tokenizing every word of tweet
        tweet_word = preprocess.clean_stopwords(tweet_word)#removing stopwords from list of words
        sent_score = 0 #initially sentiment score is 0
        for word in tweet_word: #accessing tweet word by word
            word=word.lower()   #converting word to lower case because all words in sentiment file are in lower case
            word=preprocess.clean_data(word)#removing punctuations and url's from tweets
            
            if not (word.encode('utf-8', 'ignore') == ""):
                if word.encode('utf-8') in sentiment.keys():#checking if word from tweet is present in sentiment file
                    sent_score = sent_score + int(sentiment[word])  #calculating sentiment score of word

                else:
                    sent_score = sent_score

            if word not in space:
                print (word.encode("utf-8"),int(sent_score))#printing the result to stdout

    
    
if __name__ == '__main__':
    main()

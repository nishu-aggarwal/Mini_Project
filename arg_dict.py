import json

def sentiment_dict(sentimentData):
    
    afinnfile = open(sentimentData)
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t") 
        scores[term] = float(score)  

    afinnfile.close()
    return scores 
    

def tweet_dict(tweetsdata):

    tweets=open(tweetsdata)
    tweet_text=[]
    for line in tweets:
		tweet = json.loads(line)
		if 'text' in tweet:
			text = tweet['text'].lower()
			tweet_text.append(text.encode('utf-8'))
    return tweet_text

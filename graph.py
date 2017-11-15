import matplotlib.pyplot as plt
import preprocess

def plot(tweet_scores,total_tweets):

    height=[]
    pos=0
    neg=0
    neutral=0
    for scores in tweet_scores:
        if scores>0:
            pos=pos+1
        elif scores<0:
            neg=neg+1
        else:
            neutral=neutral+1

            
    height.append(pos)
    height.append(neg)
    height.append(neutral)
    
    labels=['Positive Tweets','Negative Tweets','Neutral Tweets']
    left=[1,2,3]
    plt.bar(left,height,tick_label=labels,width=0.8,color=['red','blue','green'])

    plt.ylabel('Frequency')
    plt.title('Sentiment Analysis')

    plt.show()

    


def new_tweet_score(tweets,sentiment,term_sentiments):

    new_score=[]
    total=0
    
    for tweet in tweets:
        tweet_score=0
        total+=1
        tweet_words=tweet.split()
        tweet_words=preprocess.clean_stopwords(tweet_words)
        for word in tweet_words:
            word=word.lower()
            word=preprocess.clean_data(word)

            if word in sentiment:
                tweet_score+=sentiment[word]
            else:
                tweet_score+=term_sentiments[word]

        new_score.append(tweet_score)

    

    plot(new_score,total)


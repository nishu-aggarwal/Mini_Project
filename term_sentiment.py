from __future__ import division
import sys
import json
import arg_dict
import error
import preprocess
import graph

def computeSentiment(tweets,sentiments):

        tweet_scores=[]
        term_sentiments={}
        scores_tweet=[]
        
        for tweet in tweets:
                tweet_score=0  #for every tweet set score as 0
                tweet_words=tweet.split() #tokenize every tweet
                tweet_words=preprocess.clean_stopwords(tweet_words) #remove all stowprds from list of tweets
                for word in tweet_words: #for every word in tweet
                        word=word.lower() #convert it to lower case
                        word=preprocess.clean_data(word) #preprocess data
                        
                        if word in sentiments: #if word is present in sentiment file
                                word_score=sentiments[word] #set word score as sentiment score
                                tweet_score+=word_score #add score to corressponding tweet score

                        else:
                                word_score=0
                                tweet_score+=word_score

                                
                        #add the term and its sentiment to the dictionary 
                        if word not in term_sentiments.keys():
                                term_sentiments[word]=word_score
                                
                #add the tweet and score to tweet_scores
                tweet_scores.append([tweet,tweet_score])
                #print tweet_scores

        for term in term_sentiments:

                #Now for every term in dictionary of terms check if term is in known sentiments
                if term not in sentiments:

                        #unknown terms have a base score of zero and assuming they have occured once
                        new_score=0
                        occur=1

                        #find all tweets that contain new term
                        for i in range(0,len(tweet_scores)):
                                if term in tweet_scores[i][0]:
                                        new_score+=tweet_scores[i][1]
                                        occur+=1

                        #Normalize the new score by number of occurences
                        new_score/=occur
                        term_sentiments[term]=new_score

                print term+" "+str(format(term_sentiments[term],'.3f'))

        ch=raw_input("Press y/Y to view bar graph otherwise n for exit:\n")
        if ch=='y' or ch=='Y':
                graph.new_tweet_score(tweets,sentiments,term_sentiments)
                sys.exit(-1)
        else:
                sys.exit(-1)

                
def main():
        #Error handling
        if error.check_cmd(len(sys.argv)) == True:
            words = sys.argv[1] 
            tweets = sys.argv[2]
        else:
            sys.exit(-1)

        #create dictionary of terms and their scores
        scores=arg_dict.sentiment_dict(words)

        #create dictionary of tweets
	tweet_text=arg_dict.tweet_dict(tweets)

        #compute sentiment of terms
        computeSentiment(tweet_text,scores)
        


if __name__ == '__main__':
    main()

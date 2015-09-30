from __future__ import division
import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	


def main():
    sent_file = open(sys.argv[1]) #AFINN-111.txt, contains pre-computed sentiment scores
    tweet_file = open(sys.argv[2]) #output.txt
    scores_sentfile = {} # initialize an empty dictionary
    scores_tweetfile={} #want scores of each tweet, then use that to determine the
    #scores of terms in that tweet that aren't in sent_file
    words_notin_sentfile = []
	
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores_sentfile[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
	
    tweet_list_dict=[] # initialize empty list for tweets
	#list stores entries in order, but dictionary doesn't since its a hashtable with key-values
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            #parse the json data in output.txt and returns a python dictionary
            tweet_list_dict.append(tweet['text'].encode('utf-8'))
	
    for item in tweet_list_dict:
        tweetwords = item.split()
		#item is a dictionary of the words in each tweet
        sentiment=0
        for word in tweetwords:
            if scores_sentfile.has_key(word):
                sentiment = sentiment  + scores_sentfile[word]
            elif word not in words_notin_sentfile:
                words_notin_sentfile.append(word)
            else:
                continue
        scores_tweetfile[item] = sentiment
		
    for words_ni_sf in words_notin_sentfile:
        ns_sentiment=0
        num_tweets=0
        for item in tweet_list_dict:
            if words_ni_sf in item:
                ns_sentiment =  scores_tweetfile[item] + ns_sentiment
                num_tweets=num_tweets+1
        if num_tweets>0:
            avg_sentiment = ns_sentiment/num_tweets
            print words_ni_sf, ' ', avg_sentiment
		#print ns_sentiment
				
	
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

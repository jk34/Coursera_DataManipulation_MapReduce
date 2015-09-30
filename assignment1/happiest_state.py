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
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores_sentfile[term] = float(score)  # Convert the score to an integer.

    #example entry in output.txt
	#"place":{"id":"b69a01abdfcc087d", .., "place_type":"city","name":"Quartzsite","full_name":"Quartzsite, AZ","country_code":"US","country":"United States", ..}
	
    tweet_list_dict=[] # initialize empty list for tweets
	#list stores entries in order, but dictionary doesn't since its a hashtable with key-values
    for line in tweet_file:
        tweet = json.loads(line)  #parse the json data in output.txt and returns a python dictionary
        tweet_list_dict.append(tweet)
	
	sentiment_per_state={}
	numtweets_per_state={}
	avg_per_state={}
	
    for item in tweet_list_dict:
        tweetwords = item.get("text", "").encode('utf-8').split()
        sentiment_pertweet=0
        for word in tweetwords:
            if scores_sentfile.has_key(word):
                sentiment_pertweet = sentiment_pertweet  + float(scores_sentfile[word])
        try:
            country = item['place']['country']
            fn = item['place']['full_name'].encode('utf-8')
            sp = fn.split()
            state = sp[-1]
        except (KeyError, TypeError):
            continue
        if country=='United States':	    
            if sentiment_per_state.has_key(state):
                sentiment_per_state[state] = sentiment_per_state[state] + float(sentiment_pertweet)
                numtweets_per_state[state]=numtweets_per_state[state]+1
            else:
                sentiment_per_state[state] = sentiment_pertweet
                numtweets_per_state[state]=1
	
    happiest_state = ""
    for state in sentiment_per_state:
        avg_per_state[state] = sentiment_per_state[state]/numtweets_per_state[state]
        if happiest_state == "" or avg_per_state[state]>happiest_state:
            happiest_state=state
	
    print happiest_state
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	
def sentiment_per_tweet(tweetwords, scores_sentfile):
	sentiment=0
	for word in tweetwords:
		if scores_sentfile.has_key(word):
			sentiment = sentiment  + scores_sentfile[word]
	print sentiment
	#want to print sentiment of each tweet, each of which is the sum
	#of the sentiment scores for each term in the tweet

def main():
    sent_file = open(sys.argv[1]) #AFINN-111.txt, contains pre-computed sentiment scores
    tweet_file = open(sys.argv[2]) #output.txt
    scores_sentfile = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores_sentfile[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
	
	#list stores entries in order, but dictionary doesn't since its a hashtable with key-values
    n=0
    for line in tweet_file:
        tweet = json.loads(line)  #parse the json data in output.txt and returns a python dictionary
        if 'text' in tweet:
            ttext=tweet['text'].encode('utf-8')
            tweetwords = ttext.split()
            sentiment_per_tweet(tweetwords, scores_sentfile)
            n+=1
            print 'this is', n			 
    print n
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

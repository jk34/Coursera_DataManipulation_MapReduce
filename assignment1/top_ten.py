import sys
import json


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	

def main():
    tweet_file = open(sys.argv[1]) #output.txt

    num_each_hashtag={}
    for line in tweet_file:
        tweet = json.loads(line)  #parse the json data in output.txt and returns a python dictionary
        #tweet_list_dict.append(tweet)
		
		#example tweet:
		#{"created at":"Mon Sep..", ...,"text":"...", "entities":{"hashtags":[], ..}, ...}
        if 'entities' in tweet.keys():
            hashtags = tweet['entities']['hashtags']
            for eachtag in hashtags:
                item = eachtag['text'].encode('utf-8')
                if num_each_hashtag.has_key(item):
                    num_each_hashtag[item]+=1
                else:
                    num_each_hashtag[item]=1
	
    topsorted=sorted(num_each_hashtag, key=lambda x: num_each_hashtag[x], reverse=True)
    topsorted = topsorted[:min(10, len(topsorted))]

    for k, v in sorted(num_each_hashtag.items(), key=lambda x: x[1], reverse=True)[:10]:
        print k, ' ',float(v)
	#sorts according to x[1], which is the second element of each entry in num_each_hashtag
	#which is the value of num_each_hashtag. Thus, sort according to the top 10 highest values of num_each_hashtag
    #because x represents each item, for ex: (EclipseLunar, 5)

if __name__ == '__main__':
    main()

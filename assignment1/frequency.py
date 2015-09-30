from __future__ import division
import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	
def main():
    tweet_file = open(sys.argv[1]) #output.txt
    	
    tweet_list_dict=[] # initialize empty list for tweets
	#list stores entries in order, but dictionary doesn't since its a hashtable with key-values
    
	
    term_dict={} #store every term
	
    total_terms=0
	
    for line in tweet_file:
        tweet = json.loads(line)  #parse the json data in output.txt and returns a python dictionary
        #tweet_list_dict.append(tweet)
	
        if 'text' in tweet:
            #tweetwords = tweet['text'].strip().replace("\r","").replace("\n","").encode('utf-8')
            #tweetwords = ''.join(tweetwords.split())
            #stweetwords = tweetwords.split(' ')
            #for word in stweetwords:
            tweetwords=tweet['text'].encode('utf-8').split()
            for word in tweetwords:
                word=word.strip()
                if term_dict.has_key(word):
                    term_dict[word] += 1
                else:
                    term_dict[word] = 1
                total_terms +=1
			
	#for word in term_dict:
	#   freq = float(term_dict[word])/total_terms
    #    print word.encode("utf-8") + " " + term_dict[word]
    for word in term_dict:
        print word, ' ', float(term_dict[word])/total_terms

		
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

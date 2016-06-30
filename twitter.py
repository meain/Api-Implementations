'''
Get tweets based on a query
'''

# Wrapper used https://github.com/bear/python-twitter
# Get the api used by using $ pip install python-twitter
import twitter
from apikeys import *

#These are the keys to be used in the script
CONSUMER_KEY = key_twitter.CONSUMER_KEY
CONSUMER_SECRET = key_twitter.CONSUMER_SECRET

OAUTH_TOKEN = key_twitter.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = key_twitter.OAUTH_TOKEN_SECRET

#get the api object based on the keys
def get_api():
    api = twitter.Api(consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=OAUTH_TOKEN,
        access_token_secret=OAUTH_TOKEN_SECRET)
    print type(api)
    print api
    return api

#get the tweets as per the querries, returns a json object
#The first input is the querry(the search term) - this is the only non optional data to be provided in the function
#The second parameter is the language the tweet is
#The third parameter is the count of tweets to be obtained
def get_tweets(f_term, f_lang = 'en', f_result_type = 'recent', f_count = 10, f_max_id = ''):
    api = get_api()
    data = api.GetSearch(term=f_term, lang=f_lang, result_type=f_result_type, count=f_count, max_id=f_max_id)
    return data


def main():
    #Test inputs
    search = get_tweets('life')
    for t in search:
        print t.user.screen_name + ' (' + t.created_at + ')'
        #Add the .encode to force encoding
        print t.text.encode('utf-8')
        print ''

if __name__ == '__main__':
    main()

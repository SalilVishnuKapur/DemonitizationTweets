import tweepy
import textblob
from textblob import TextBlob
from TwitterAPI import TwitterAPI
import tweepy, datetime, time

consumer_key= 'cWZK5YanFHg5bRTJIzODiXMMg'
consumer_secret = '6qa2n28N4HbFWOJ7VGLZCEF9exBPs7prrcLQFt6dqcNLtA7caV'
access_token = '3163577036-aoNxlLUZa0x8SOgXz1TfPqybpD1NXqzntjakgN8'
access_secret = 'Otd5K9t8pA4jakZy7iII3UAl62KlGIW7ZflFjIqIVFjMR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

my_dict = {}
tweets = api.search(q="demonitization")
      
for tweet in tweets:
   # Create a key value pair 
   # key date
   # Count  
   my_dict[tweet.created_at] = 1
   print(my_dict);

# Substitute your API and ACCESS credentials.
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)
r = api.request('statuses/filter', {'track':'giraffe'})
for item in r:
  print(item['text'])

count = 0
skip = 0
r = api.request('statuses/filter', {'track':'giraffe'})
for item in r:
  if 'text' in item:
   count += 1
  elif 'limit' in item:
   skip = item['limit'].get('track')
   print('*** SKIPPED %d TWEETS' % skip)
  elif 'disconnect' in item:
   print('[disconnect] %s' % item['disconnect'].get('reason'))
   break
  print(count+skip);


my_dict = {}
tweets = api.request('statuses/filter', {'track':'demonitization'})
      
for tweet in tweets:
   # Create a key value pair 
   # key date
   # Count  
  if 'text' in tweet:      
     my_dict[tweet.created_at] = 1
  elif 'limit' in item:
     skip = item['limit'].get('track')
     print('*** SKIPPED %d TWEETS' % skip)
  elif 'disconnect' in tweet:
     print('[disconnect] %s' % item['disconnect'].get('reason'))
     break
  print(my_dict);


      
get_tweets(api, "anmoluppal366")

for key in tokens:
  public_tweets= api.search(key)
  for tweet in public_tweets:
     print(tweet.text)
     analysis= TextBlob(tweet.text)
     print(analysis.sentiment)

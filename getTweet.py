import tweepy
import textblob
from textblob import TextBlob

class tweet {

    def initialize():
      consumer_key= 'cWZK5YanFHg5bRTJIzODiXMMg'
      consumer_secret = '6qa2n28N4HbFWOJ7VGLZCEF9exBPs7prrcLQFt6dqcNLtA7caV'
      access_token = '3163577036-aoNxlLUZa0x8SOgXz1TfPqybpD1NXqzntjakgN8'
      access_secret = 'Otd5K9t8pA4jakZy7iII3UAl62KlGIW7ZflFjIqIVFjMR'
      tokens = ['Real Estate', 'home loans', 'auto industry', 'tourism', 'stock market', 'wedding', 'Jobs', 'Black money', 
                'Migrant Workers', 'Labour', 'Cash', 'money', 'cashless', 'EMI rates', 'digital', 'PayTM', 'ATM', 'Lending rates',        
                'RBI', 'digital', 'poor', 'rich', 'm-wallets', 'business', 'trade', 'market', 'loss','gain', 'benefit',  'good', 'bad',        
                'politics', 'pro-poor', 'pro-rich', 'death', 'clean india', 'corruption', 'terrorism', 'counterfeit currency', 'fake notes', 
                'jan dhan', 'zero-balance accounts', 'implementation']


 
    ##### TODO : 
    #   Understand the Temporal Change - How frequent are the tweets – tweet frequency as a function of time
    #####
    def Q1(token, api):
      my_dict = {}
      tweets = api.search(q=token)      
      for tweet in tweets:
        # Create a key value pair 
        # key date
        # Count  
        my_dict[tweet.created_at] = 1
        print(my_dict);
      return my_dict

    ##### TODO : 
    #   What are the commonly used words – how does their frequency change over the period of time
    #####  
    def Q2():
      #  word map and later solve

    ##### TODO : 
    #   How influential the people are who tweet on the topic – how many replies/comments do their tweets get
    #####
    def Q3():
      #  x people name
      #  y number of tweets
 
    ##### TODO : 
    #   How many of them are influential on the bases of replies?
    #####
    def Q4():
      #  x people name
      #  y number of replies 

    ##### TODO : 
    #   Understand the spatial change –how the sentiment was in different states in the country
    #####
    def Q5():
      #  x state name
      #  y sentiment

    def main():
      auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      auth.set_access_token(access_token, access_secret)
      api = tweepy.API(auth)
      
      ### Q1 Soln
      Ans = Q1("demonitization",api)
       
}

import os
import time

import tweepy

class EndlessStream(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        #print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        print status.text
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

class TwitterAPI:
    """
    Class for accessing the Twitter API.

    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
    """
    def __init__(self):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        """Send a tweet"""
        self.api.update_status(message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    listener = EndlessStream()
    stream = Stream(twitter.auth, listener)
    stream.filter(track=['gamergate is'])
    # twitter.tweet("Hello world!") #You probably want to remove this line
    #while True:
    #    for tweet in tweets:
    #        usr = tweet.user.screen_name
    #        message = "@%s Actually, it's about ethics in games journalism. #GamerGate" % usr
    #        twitter.tweet(message)
    #        time.sleep(30)
    

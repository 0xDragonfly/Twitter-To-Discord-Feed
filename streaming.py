import tweepy
import config
import requests
import re
import time
from get_twitter_IDs import get_follower_IDs
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone

# Connect to the API again:
auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY,config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN,config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Get your list of follower IDs:
username = "@Your-twitter-username-here"
id_list = get_follower_IDs(api, username)

# Avoiding possible rate limit after getting follower IDs, twitter changes this cooloff frequently
time.sleep(60)

# Create Websocket connection class, with various states for websocket:
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            if str(status._json['user']['id']) in id_list:

                # Get tweet for specific follower ID:
                status.text = re.sub(r'http\S+', '', status.text)
                tweet_link = f"https://twitter.com/{status._json['user']['screen_name']}/status/{status._json['id']}"

                # Compose message to post to Discord server
                chat_message1 = {
                    "username":status._json['user']['name'],
                    "avatar_url":status._json["user"]['profile_image_url_https'],
                    "content":f"{status.text}\n{tweet_link}"
                }

                # Post to Discord Server using requests 
                requests.post(config.discord_wh_link,json=chat_message1)
                
        except Exception as e:
            print(e)
            print("Stream disconnected")

            # Finding time when stream disconnected for debugging purposes:
            local_tz = get_localzone()
            tz = timezone(str(local_tz))
            current_time = datetime.now(tz)

            # Relaying stream disconnected message to discord:
            chat_message1 = {
                        "content":f"Twitter feed disconnected at {current_time.strftime('%Y-%m-%d_%H-%M-%S')}"
                    }

            requests.post(config.discord_wh_link,json=chat_message1)
    
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
    
    def on_closed(self, resp):
        """This is called when the stream has been closed by Twitter."""
        print("Stream connection closed by Twitter")
    
    def on_connect(self):
        """This is called after successfully connecting to the streaming API."""
        print("Stream connected")
    
    def on_connection_error(self):
        """This is called when the stream connection errors or times out."""
        print("Stream connection has errored or timed out")
    
    def on_disconnect(self):
        """This is called when the stream has disconnected."""
        print("Stream disconnected")
        local_tz = get_localzone()
        tz = timezone(str(local_tz))
        current_time = datetime.now(tz)

        chat_message1 = {
                    "content":f"Twitter feed disconnected at {current_time.strftime('%Y-%m-%d_%H-%M-%S')}"
                }

        requests.post(config.discord_wh_link,json=chat_message1)
    
    def on_exception(self, exception):
        """This is called when an unhandled exception occurs."""
        print("Stream encountered an exception")

    def on_keep_alive(self):
        """This is called when a keep-alive signal is received."""
        print("Received keep-alive signal")

    def on_request_error(self, status_code):
        """This is called when a non-200 HTTP status code is encountered."""
        print("Stream encountered HTTP error: %d", status_code)

    def on_warning(self, notice):
        """This is called when a stall warning message is received."""
        print("Received stall warning: %s", notice)
        local_tz = get_localzone()
        tz = timezone(str(local_tz))
        current_time = datetime.now(tz)

        chat_message1 = {
                    "content":f"Recieved stall warning at {current_time.strftime('%Y-%m-%d_%H-%M-%S')}"
                }

        requests.post(config.discord_wh_link,json=chat_message1)

# Initialize websocket here:
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# Starting the websocket to listen for new tweets on timeline
while True:
    try:
        print("Stream Re-connected..")
        local_tz = get_localzone()
        tz = timezone(str(local_tz))
        current_time = datetime.now(tz)

        chat_message1 = {
                    "content":f"Twitter feed reconnected at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
                }

        requests.post(config.discord_wh_link,json=chat_message1)
        
        myStream.filter(follow=id_list,stall_warnings=True)

    except:
        print("Stream disconnected.. Attempting to connect again..")
        local_tz = get_localzone()
        tz = timezone(str(local_tz))
        current_time = datetime.now(tz)

        chat_message1 = {
                    "content":f"Twitter feed disconnected at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
                }

        requests.post(config.discord_wh_link,json=chat_message1)
        continue
    
    time.sleep(60)
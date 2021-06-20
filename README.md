# Twitter-To-Discord-Feed
This repo is meant to fix the annoying issue where Twitter doesn't deliver all the tweets of those you're following. All your tweets will now be delivered to your discord using webhooks.

Requirements:
Python <3.6
tweepy
requests
pytz
tzlocal

This project assumes you have access to a valid Twitter API key/tokens. 

## Intended Process Flow:  

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKFR3ZWV0cyBmcm9tIHlvdXIgdHdpdHRlciBmb2xsb3dzKSAtLT58d2Vic29ja2V0IG9wZW58IEJbVHdpdHRlciBBUEldXG4gICAgLS0-IENbUHJvY2VzcyBpbmNvbWluZyByYXcgZGF0YV0gLS0-IERbRXh0cmFjdCBUd2VldCBpbmZvLCBkYXRlLCBsaW5rc11cbiAgICAtLT4gRVtQb3N0IGV4dHJhY3RlZCBpbmZvIHRvIG91ciBEaXNjb3JkLCBhbmQgcmVuZGVyIHByb3Blcmx5XVxuICAgIC0tPiBGKENoZWNrIHByb2Nlc3NlcyBmb3IgZXJyb3JzL2Rpc2Nvbm5lY3RzKSAtLT58UmVjb25uZWN0IGlmIGRyb3BwZWR8QlxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKFR3ZWV0cyBmcm9tIHlvdXIgdHdpdHRlciBmb2xsb3dzKSAtLT58d2Vic29ja2V0IG9wZW58IEJbIFR3aXR0ZXIgQVBJXVxuICAgIC0tPiBDW1Byb2Nlc3MgaW5jb21pbmcgcmF3IGRhdGFdIC0tPiBEW0V4dHJhY3QgVHdlZXQgaW5mbywgZGF0ZSwgbGlua3NdXG4gICAgLS0-IEVbUG9zdCBleHRyYWN0ZWQgaW5mbyB0byBvdXIgRGlzY29yZCwgYW5kIHJlbmRlciBwcm9wZXJseV1cbiAgICAtLT4gRihDaGVjayBwcm9jZXNzZXMgZm9yIGVycm9ycy9kaXNjb25uZWN0cykgLS0-fFJlY29ubmVjdCBpZiBkcm9wcGVkfEJcbiIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)  

## Steps to take in discord
1. You’ve either gotta be the owner of the server (just make a new one) or have one where you’ve got admin rights. Make a new text channel, with any name you want.  

2. Once that’s done, right click on the server name, head to server settings and then integrations.  

3. You’ll need to make a new webhook, so click the “view webhooks” arrow.  

4. Click on the “New Webhook” button, and you should see a section where you can enter the webhook name and channel. Make sure you’ve got the right channel selected.  

5. Click on Copy Webhook URL and save that somewhere, you’ll be using it soon.  

## Where to add your username/API keys:
1. Enter your twitter API details in the config.py file, as well as that discord webhook you just created.  

2. Now head to the streaming.py file, and enter your username in line 17, without removing the @ symbol.  

## To run the script
```
pip install -r requirements.txt
python streaming.py
```

## To stop the script
Because tweepy glitches out every so often and we don’t want our feed getting cut off, we’re running the process on an endless loop. So to exit out or stop the feed, you can either close the terminal altogether, or press Ctrl+z.


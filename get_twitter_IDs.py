import tweepy
import config

def get_follower_IDs(api, username):
    try:
        # Finding follower IDs of the accounts you want your feed to connect to
        follower_list = []
        for friend in tweepy.Cursor(api.friends,id=username).items():
            # Process the friend here
            follower_list.append(friend)

        follower_dict = {}
        for item in follower_list:
            new_dict = {item._json["id"]:item._json["name"]}
            follower_dict.update(new_dict)

        id_list = []
        for keys in follower_dict:
            id_list.append(str(keys))

        return id_list
    except Exception as e:
        print(f"Encountered Error {e}")
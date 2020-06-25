import tweepy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
f = open('Tweet.txt', 'r')
Tweet = f.read()
if len(Tweet) < 281:
    print("____________________________________")
    print("")
    print(Tweet)
    print("")
    print("____________________________________")
    print("Tweet has " + str(len(Tweet)) + " characters")
    confirm = input("Tweet this? (yes/no): ")
    if confirm == "yes":
        api.update_status(Tweet)
        print("")
        print("Tweet send successfully")
    else:
        print("Tweet confirmation error")
else:
    print("____________________________________")
    print("")
    print("The Tweet is to long, it has " + str(len(Tweet)) + " characters")
    print("")
    print("____________________________________")
f.close()

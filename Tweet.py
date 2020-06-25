import tweepy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("V75KfMFFSHthOKCjoBNAQnYnS", "nGywmAkfScOQzefdaLcaCzuceS8vIseF2gZgiJDjvsDHjKEtFb")
auth.set_access_token("3208340651-bOyMVzWGAYWkgMGf5UD6c7qWVjI61yr7gCLMPXN", "keocAcpdJA4yTn3e0CJKgL95Df1H4DzQnAcvm0wc9uxeG")

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
import twitter_handling as tw
import image_processing as imagp

twitter = tw.twitter_feed_catching("keys")

# consider wrong user id input 
username = input("Twitter ID: ")
profile_url = twitter.get_user_pic(username)
tweets = twitter.get_users_tweets(username)

# creat image and store into folder
imagp.create_images(username, profile_url, tweets)
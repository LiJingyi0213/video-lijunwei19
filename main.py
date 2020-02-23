import twitter_handling as tw
import image_processing as imagp
import ImageToVideo as ITV
import threading
import time
import queue


def grab_tweets_process(q,completion_queue):
    username = q.get()
    profile_url = twitter.get_user_pic(username)
    tweets = twitter.get_users_tweets(username)
    imagp.create_images(username, profile_url, tweets)
    completion_queue.put(username)


def video_process(completion_queue):
    username =  completion_queue.get()
    ITV.imgToVideo(username) 

if __name__ == '__main__':
  q1 = queue.Queue(maxsize=20)
  completion_q1 = queue.Queue()
  twitter = tw.twitter_feed_catching("keys")

  while True:
    if not q1.full():
      id = input("Twitter id?")
      q1.put(id)
    else:
      print("wait a minute...")
    if not q1.empty():
      t1 = threading.Thread(name="grab_tweets_process", target=grab_tweets_process, args=(q1, completion_q1))
      t1.start()    
    if not completion_q1.empty():
      t2 = threading.Thread(name="video_process", target=video_process, args=(completion_q1))
      t2.start()
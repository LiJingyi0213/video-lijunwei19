import twitter_handling as tw
import image_processing as imagp
import ImageToVideo as ITV
import threading
import time
import queue


def grab_tweets_process(q,completion_queue):
    username = q.get()
    print("\ngrab "+username+" tweets is processing...")
    profile_url = twitter.get_user_pic(username)
    tweets = twitter.get_users_tweets(username)
    imagp.create_images(username, profile_url, tweets)
    completion_queue.put(username)
    print("\ndone")


def video_process(q1, completion_queue):
    if not completion_queue.empty():
      username =  completion_queue.get()
      print("\n"+username+" image to video is processing...")
      ITV.imgToVideo(username) 
      print ("\n"+"done")


def ID_input (q1, completion_queue):
    if not q1.full():
      id = input("\n Twitter id ?")
      q1.put(id)
    else:
      print("\n wait a minute...")
    time.sleep(0.2)
    return ID_input (q1, completion_queue)


if __name__ == '__main__':
  q1 = queue.Queue(maxsize=20)
  completion_q1 = queue.Queue()
  twitter = tw.twitter_feed_catching("keys")

  t0 = threading.Thread(name="twitter_ID input",target= ID_input, args=(q1, completion_q1))
  t0.start()

  while True:
    if not q1.empty():
      t1 = threading.Thread(name="grab_tweets_process", target=grab_tweets_process, args=(q1, completion_q1))
      t1.start()  
    time.sleep(.1)  
    if not completion_q1.empty():
      t2 = threading.Thread(name="video_process", target=video_process, args=(q1, completion_q1))
      t2.start()
    time.sleep(.1)  


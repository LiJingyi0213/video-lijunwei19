import os
import subprocess

def imgToVideo(username):
  fileName =  'processed_imgs/'+ username +'img' +'%d'+'.png'
  normalVideo =  "video/"  + username + "normal.avi"
  betterVideo =  "video/"  + username + "better.mp4"

  # convert jpg to mp4
  # ffmpeg -i img-%02d.png video_name.avi #2-digit number for name
  # set frame rate
  # ffmpeg -framerate 30 -i img%03d.png output.mp4  
  # 0.3 for frame rate = 3s per image    
  subprocess.call(['ffmpeg', '-framerate', '0.3', '-i', 
    fileName, 
    normalVideo])

  # convert to better quality
  subprocess.call(['ffmpeg', '-i', normalVideo, '-c:a', 'copy', 
    '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
    betterVideo])

imgToVideo('IBM')
import requests
import textwrap
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import twitter_handling as twh

def create_images(user_id, profile_url, tweets):
    count = 0;
    for tweet in tweets:
      try :
        print(tweet.full_text)
        txt = tweet.full_text
      except AttributeError:
        return
      print(count)
      count = count +1
      font = ImageFont.truetype(r'character_type/arial.ttf', 14)
      background = Image.new('RGBA', (1024, 768), (255, 255, 255, 255))
      response = requests.get(profile_url)
      img = Image.open(BytesIO(response.content))
      draw = ImageDraw.Draw(background)
      lines = textwrap.wrap(txt, width=120)
      x, y = 50, 225
      for line in lines:
          width, height = font.getsize(line)
          draw.text(((x), y), line, font=font, fill="black")
          y += 15
      draw.text((120, 170), user_id, font=font, fill="black")
      offset = (50, 150)
      background.paste(img, offset)
      background.save(r'processed_imgs/'+ user_id +'_''img'+str(count)+'.png')

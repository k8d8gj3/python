import requests
import re
import datetime
from PIL import Image, ImageFont, ImageDraw 

res = requests.get("https://covid19.who.int/page-data/measures/page-data.json", {
  "headers": {
    "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
    "sec-ch-ua-mobile": "?0"
  },
  "referrer": "https://covid19.who.int/table",
  "referrerPolicy": "same-origin",
  "body": None,
  "method": "GET",
  "mode": "cors",
  "credentials": "omit"
})

yesterday = datetime.date.today() - datetime.timedelta(days=1)

confirmed = re.search('("IL":\{"day":"'+ str(yesterday) +'.*?"Confirmed":)(\d*)', res.content.decode()).group(2)

image = Image.open("nature.jpg")

title_font = ImageFont.truetype('Roboto-Black.ttf', 150)

title_text = f"Corona update: {confirmed}"

image_editable = ImageDraw.Draw(image)

image_editable.text((6700,300), title_text, (0, 0, 0), font=title_font)

image.save("result.jpg")

# Change desktop image to result.jpg
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\roee1\\Desktop\\python\\corona-update\\result.jpg" , 0)
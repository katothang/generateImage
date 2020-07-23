from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import random
import os
import uuid
letters = 'abcdefghijklmnopqrstuvwxyz0123456789'

for i in range(1000):
    letter = random.choice(letters)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    fontSize = random.randint(20,40)
    img = Image.new('RGB', (30, 60), color = 'white')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", fontSize)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((7, 10), letter ,(r, g, b), font=font)
    if not os.path.exists(f"test"):
        os.mkdir(f"test")
    img.save(f'test/{str(uuid.uuid1())}.jpg')
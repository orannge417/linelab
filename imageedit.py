from PIL import Image, ImageDraw
import os 

def imageedit(src: str, desc: str, size = 800):
    
    im = Image.open(src)
    draw = ImageDraw.Draw(im)

    if im.width > size:
        proportion = size / im.width
    im = im.resize((int(im.width * proportion), int(im.height * proportion)))

    text = "apple!"


    # テキストの周りの5pxずつに余白を作る
    x = 10
    y = 10
    margin = 5
    text_width = draw.textsize(text)[0] + margin
    text_height = draw.textsize(text)[1] + margin
    draw.rectangle(
    (x - margin, y - margin, x + text_width, y + text_height), fill=(255, 255, 255)
    )
    # テキスト描画
    draw.text((x, y), text, fill=(0, 0, 0))

    im.save(desc)


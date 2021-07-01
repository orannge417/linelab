from PIL import Image, ImageDraw, ImageFont
import os 

def imageedit(image=None):
    
    try:
        os.remove("data/image.png")
    except FileNotFoundError:
        print("hoge")

    if image is None:
        return 0
    
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    size = 800
    if im.width > size:
        proportion = size / im.width
    im = im.resize((int(im.width * proportion), int(im.height * proportion)))

    text = "apple!"

    # フォントの読み込み
    font = ImageFont.truetype("./fonts/Harlow Solid Regular.ttf", 60)

    # テキストの周りの5pxずつに余白を作る
    x = 10
    y = 10
    margin = 5
    text_width = draw.textsize(text, font=font)[0] + margin
    text_height = draw.textsize(text, font=font)[1] + margin
    draw.rectangle(
    (x - margin, y - margin, x + text_width, y + text_height), fill=(255, 255, 255)
    )
    # テキスト描画
    draw.text((x, y), text, fill=(0, 0, 0), font=font)

    im.save("//data//image.png")

    return 'a'

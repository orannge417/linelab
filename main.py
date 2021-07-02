# LINE BOT のサンプルからいじる
# https://qiita.com/sayama0402/items/e2c9e65786259dc55e11
# https://qiita.com/tamago324/items/4df361fd6ac5b51a8a07

from io import BytesIO

from linebot.models.send_messages import ImageSendMessage
from imageedit import imageedit
from flask import Flask, request, abort
from pathlib import Path

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

from linebot.models.messages import ImageMessage

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

@handler.add(MessageEvent, message=ImageMessage)
def handleimage(event):
    # メッセージのIDを取得
    # message_id = event.message.id

    
    # src_image_path = Path("data/images/{}.jpg".format(message_id)).absolute()
    # main_image_path = "data/images/{}_main.jpg".format(message_id)
    # preview_image_path = "data/images/{}_preview.jpg".format(message_id)

    # # 画像を保存
    # save_image(message_id, src_image_path)

    # imageedit(src=src_image_path, desc=Path(main_image_path).absolute())



    # image_message = ImageSendMessage(
    #     main_content_url = f"https://linebotforlab2.herokuapp.com/{main_image_path}",
    #     preview_image_url = f"https://linebotforlab2.herokuapp.com/{preview_image_path}",
    # )

    # app.logger.info(f"https://linebotforlab2.herokuapp.com/{main_image_path}")

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='This is image'))


    line_bot_api.reply_message(event.reply_token, image_message)

# def save_image(message_id: str, save_path: str) -> None:
#     """保存"""
#     message_content = line_bot_api.get_message_content(message_id)
#     with open(save_path, "wb") as f:
#         for chunk in message_content.iter_content():
#             f.write(chunk)

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
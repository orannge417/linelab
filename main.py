# LINE BOT のサンプルからいじる
# https://qiita.com/sayama0402/items/e2c9e65786259dc55e11
# https://qiita.com/tamago324/items/4df361fd6ac5b51a8a07

from io import BytesIO

from linebot.models.send_messages import ImageSendMessage
# from linebot2.imageedit import imageedit
from flask import Flask, request, abort

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
    # # メッセージのIDを取得
    # message_id = event.message.id
    
    # # message_idから画像のバイナリーデータを取得
    # message_content = line_bot_api.get_message_content(message_id)

    # image = BytesIO(message_content.content)

    # result = imageedit(image)

    # if isinstance(result, int):
    #     TextSendMessage(text='Image is not processed successfully')
        
    # elif isinstance(result, str):
    #     # main_image_path= f"data/image.png"

    #     ImageSendMessage(result)

    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text='This is image.'))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
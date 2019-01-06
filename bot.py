#!/usr/bin/env python3

import os
import logging
from PIL import Image
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from img_to_hearts import img_to_hearts

logger = logging.getLogger()
logger.setLevel(logging.INFO)

EXT = '.jpg'
IMAGES_PATH = os.getenv("IMG_PATH")
TOKEN = os.getenv("TOKEN")
PROXY = os.getenv("PROXY_URL")
REQUEST_KWARGS = {
    'proxy_url': PROXY,
}


def start(bot, update):
    msg = "Я бот, который сделает из фото изображение из сердечек! Отошли мне изображение, чтобы попробовать!"
    bot.send_message(chat_id=update.message.chat_id, text=msg)


def img_to_heart(bot, update):
    file_id = update.message.photo[-1].file_id
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Класс! Картинка! Уже начинаю обработку..")
    # обработать
    new_file = bot.get_file(file_id)
    source_file = os.path.join(IMAGES_PATH, f"{file_id}{EXT}")
    heart_file = os.path.join(IMAGES_PATH, f"hearted_{file_id}{EXT}")
    new_file.download(source_file)
    img = img_to_hearts(Image.open(source_file))
    img.save(heart_file)
    # залить и переслать
    bot.send_photo(chat_id=chat_id, photo=open(heart_file, 'rb'))


def main():
    updater = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    img_handler = MessageHandler(Filters.photo, img_to_heart)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(img_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

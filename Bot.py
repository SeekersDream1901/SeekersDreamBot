# t.me/SeekersDreamBot - ссылка на бота в телеграме
# 5208831167:AAEn8_jBBjwfppuKZjODFObielnH0ZMxSn0 токкен

import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters       #Импортируем файл апдейтера, библиотека командхандлер(для разделения потоков пользователей,)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)

def start_bot (update: Updater, context: CallbackContext):
	mytext = """Приветствую, {} в телеграм боте "SeekersDream"
SeekersDream Предоставляет ряд услуг с которымы Вы можете ознакомиться подробнее чуть позже,
Когда данная часть бота будет дописана,но пока что я знаю только команду /start =)""".format(update.message.chat.first_name)
	update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
	text = update.message.text
	logging.info(text)

	update.message.reply_text(text)

def main():
	updtr = Updater(settings.TOKEN_TELEGRAMM)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__== "__main__":
	logging.info('Bot started!')
	main()
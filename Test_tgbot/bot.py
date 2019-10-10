#Подключения
import telebot
from telebot import types #Для клавы

#Токен
token = "928921351:AAG9PyI0ZLiN04fDChBDYZ2uvk9oat1rTpE"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def Text_Msgs(message):
    bot.send_message(message.chat.id, "Как настроение ?")
    markup = types.ReplyKeyboardMarkup()
    markup.row("\U0001F60A")
    markup.row("\U0001F645", "\U0001F63A")

if __name__ == '__main__':
    bot.polling(none_stop=True)



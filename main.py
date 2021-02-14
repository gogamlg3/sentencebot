import telebot

bot = telebot.TeleBot('1688264550:AAEcStee7FHgO_ftiIs4had9K1vPBBojPJ0')
chatID = '982129685'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Жду картиночки (* ^ ω ^)')

@bot.message_handler(content_types=['photo'])
def photo_messages(message):
    bot.forward_message(chatID, message.chat.id, message.message_id)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'рома гей':
        bot.send_message(message.from_user.id, 'согласен')
    else:
        bot.send_message(message.from_user.id, 'Пришли фотографию для канала.')

bot.polling()







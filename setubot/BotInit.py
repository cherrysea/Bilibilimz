import random
import time
import telebot
import BotConfig, GetSetu


random.seed(time.time())

TOKEN = '1829725347:AAGEUC1uVH5PLfbN5s1Wu645SG2Qtwdzr8A'

bot = telebot.TeleBot(BotConfig.TOKEN, parse_mode=None)

# bot.send_message(BotConfig.chat_id, '你寄吧谁')

# 定义 /start 和  /help 命令
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Howdy, how are you doing?')

# 将所有传入的文本消息回显给发件人。它使用 lambda 函数来测试消息。如果 lambda 返回 True，则消息由装饰函数处理。
# 因为我们希望所有消息都由这个函数处理，所以我们总是简单地返回 True。
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# 儒雅随和
# @bot.message_handler(content_types=['text'])
# def send_jb(message):
#     list1 = ['傻逼', '你寄吧谁啊', '我是你爹', '操你妈', '去死', '什么玩意儿', '恶心心', '你真tm丑']
#     list2 = ['鸡掰', '粑粑粑粑', '操', '甘霖娘', '甘霖娘鸡掰', '操他妈你不要再讲了好不好', '小屁孩','好了 你不要再讲了']
#     reply = random.choice(list2)
#     bot.reply_to(message, reply)

@bot.message_handler(content_types=['text'])
def send_SeTu(message):
    if message.text == '色图':
        bot.send_message(message.chat.id, '想屁吃')
        img = GetSetu.getSetu()
        bot.send_photo(message.chat.id, img)

bot.polling()
bot.polling(none_stop=True)
bot.polling(interval=3)
while True:
    pass
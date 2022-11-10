import telepot

token = ''
channel_id = ''
bot = telepot.Bot(token)
bot.sendDocument(channel_id, open('./capture/1.png', 'rb'))

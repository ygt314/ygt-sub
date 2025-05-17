from wxpy import *
bot = Bot()
my_friend = bot.friends().search('chemistry@ygt02', sex=MALE, city="郴州")[0]
my_friend.send('Hello WeChat!')
from wxpy import *
from weather_spy import getWeather
from datetime import datetime as dt

bot = Bot()
me = bot.friends().search('小冉', sex=FEMALE)[0]

# 获取天气
weather = getWeather()
windLevel = weather["windL"]
lowTemp = weather["lowT"]
highTemp = weather["highT"]
weather = weather["weather"]
print(windLevel + lowTemp + highTemp + weather)

# 获取当前时间
cur_t = dt.now()

msg = "今天是" + str(cur_t.year) + "年" + str(cur_t.month) + "月" + str(cur_t.day) + "日\n" + \
      "现在为你播报明天的天气预报: \n" + \
      "地区：北京市\n" + \
      "最高气温：" + highTemp + "\n" + \
      "最低气温：" + lowTemp + "\n" + \
      "风速：" + windLevel + "\n" + \
      "天气：" + weather + "\n" + \
      "播报完毕，希望你今晚可以睡个好觉哦！晚安~"


print(msg)

me.send(msg)

# # 打印来自其他好友、群聊和公众号的消息
# @bot.register()
# def print_others(msg):
#     print(msg)
#
#
# # 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register(me)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)

# # 自动接受新的好友请求
# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     # 接受好友请求
#     new_friend = msg.card.accept()
#     # 向新的好友发送消息
#     new_friend.send('哈哈，我自动接受了你的好友请求')

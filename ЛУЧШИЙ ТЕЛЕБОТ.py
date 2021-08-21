import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://world-weather.ru/pogoda/kyrgyzstan/bishkek/14days/')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot("1925531327:AAHxyVygMn-_UkhyTnl2-LPu4UtN4Ds7lHw")

for el in html.select('#content'):
    t_min = el.select('.evening.fourteen-n .weather-temperature')[0].text
    t_max = el.select('.day.fourteen-d .weather-temperature')[0].text
    text = el.select('.chart-text')[0].text
    print(t_min +','+ t_max +'\n' + text)

@bot.message_handler(commands=['weather'])
def main(message):
    bot.send_message(message.chat.id,"Привет мой маленький FUCKING SLAVE:3")
    bot.send_message(message.chat.id,"Я отшлепал геодезистов и узнал для тебя погодку:\n" +
       t_min + ',' + t_max + '\n' + text)

@bot.message_handler(commands=['help'])
def say_hi(message):
    bot.send_message(message.chat.id,"Я могу говорить тебе погоду и могу послать тебя нахуй")

@bot.message_handler(commands=['ch1'])
def tl(message):
    bot.send_message(message.chat.id,"Иди нахуй")

@bot.message_handler(commands=['start'])
def po(message):
    bot.send_message(message.chat.id,"Hi, мой маленький Slave, теперь я твой личный Dungeon Master, у меня есть список команд которые ты можешь узнать введя команду /help")


if __name__ == '__main__':
    bot.polling(none_stop=True)


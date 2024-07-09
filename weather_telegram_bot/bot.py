import telebot
import weather
import gps

token = "INSERT_YOUR_TOKEN_HERE"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['weather', 'w'])
def get_weather(message):
	try:
		city = message.text.split()[1]
	except: bot.send_message(message.chat.id, "Не могу распознать вашу команду.")
	try:
		x, y = gps.coords(city)

		output_message = "Погода в городе " + city
		city = weather.get_weather(x, y)
		temperature = str(int(city.Variables(0).Value()))
		current_cloud_cover = str(city.Variables(2).Value())
		wind = str(int(city.Variables(3).Value()))
		output_message += ":\n Температура воздуха: " + temperature + "°C\n"
		output_message += " Скорость ветра: " + wind + " м/c\n"
		output_message += " Облачность: " + current_cloud_cover + "%\n"
		bot.send_message(message.chat.id, output_message)  # send result
	except:
		bot.send_message(message.chat.id, "Город не найден")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет!\nОтправь мне '/w Имя_города' чтоб получить информацию о погоде в нём\n:D")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

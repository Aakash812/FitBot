import telebot
API_KEY='API KEY'  # change this to the token you get from @BotFather
CHAT='@gym11bot'  # can be a @username or a id, change this to your own @username or id for example.

bot = telebot.TeleBot(API_KEY, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help', 'options'])
def send_welcome(message):
	bot.send_message(message.chat.id, text="To Calculate BMI, enter weight in kg and height in meters")

@bot.message_handler(func=lambda message:True)
def echo_all(message):
	weight,height = message.text.split()
	bmi = float(weight)/float(height)**2.0

	output = ""
	if bmi < 18.5:
		output = "uw"
		bot.send_message(message.chat.id, text="UnderWeight")
		bot.send_photo(chat_id=message.chat.id, photo="https://raw.githubusercontent.com/Aakash812/FitBot/main/uw.jpg")
	elif bmi >= 18.5 and bmi<=24.9:
		output = "hw"
		bot.send_message(message.chat.id, text="HealthyWeight")
		bot.send_photo(chat_id=message.chat.id, photo="https://raw.githubusercontent.com/Aakash812/FitBot/main/hw.jpg")
	elif bmi >=25 and bmi<=29.9:
		output = "ow"
		bot.send_message(message.chat.id, text="OverWeight")
		bot.send_photo(chat_id=message.chat.id, photo="https://raw.githubusercontent.com/Aakash812/FitBot/main/ow.jpg")
	else:
		output = "ob"
		bot.send_message(message.chat.id, text="Obese")
		bot.send_photo(chat_id=message.chat.id, photo="https://raw.githubusercontent.com/Aakash812/FitBot/main/ob.jpg")


bot.infinity_polling()
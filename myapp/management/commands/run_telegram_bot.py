from django.core.management.base import BaseCommand 
import telebot
from myapp.models import zat
bot = telebot.TeleBot("6808068862:AAHj9lbYBajaJArjpg6iy3BsULlwFVwHNWo")  # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['products'])
def zats(message):
	products = zat.objects.all()
	for product in products:
		response = f"Name: {product.name}, Price: {product.price}"  
		bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['add'])
def add_product(message):
    if len(message.text.split()) == 3:
        words = message.text.split()
        product_name = words[1]
        product_price = words[2]
        new_product = zat(name=product_name, price=product_price)
        new_product.save()

        bot.send_message(message.chat.id, f"Product '{product_name}' added successfully!")
    else:
        bot.send_message(message.chat.id, "Invalid format. Use: /add <product_name> <product_price>")


@bot.message_handler(commands=['help'])
def help_command(message):
    commands = [
        '/products - Show all products',
		'/start'

    ]
    bot.send_message(message.chat.id, "Available commands:\n" + "\n".join(commands))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

class Command(BaseCommand):
	def handle(self, *args, **options):
		print("Starting bot...")
		bot.polling()
		print("Bot stopped")
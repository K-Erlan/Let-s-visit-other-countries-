import telebot
from telebot import types
# Global bot setting
TOKEN = ''

# Code
PRODUCTS = {}

print('Working')
bot = telebot.TeleBot(TOKEN)

def add_category(name):
    PRODUCTS[name] = []


def add_product(to, name, price, photo):
    PRODUCTS[to].append([name, price, photo])


def get_categories_list():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for CATEGORIES in PRODUCTS:
        markup.add(CATEGORIES)
    markup.add("Помощь")
    return markup


def send_products(to, category, markup):
    for X in PRODUCTS[category]:
        bot.send_photo(to,
                       X[2],
                       reply_markup=markup,
                       caption=X[0]+"\n\nЦена: "+X[1])
# Product settings

add_category("Turkey")
add_category("France")
add_category("Germany")
add_category("Egypt")
add_category("Dubai")
add_category("Czech")
add_category("Goa")
add_category("Thailand")
add_category("Sri Lanka")
add_category("Maldives")
add_product(
 "Turkey", "Turkish Riviera (Antalya + Istanbul)",
 "599 USD, more details here-> http://putevka.kg/tours/turetskaya-rivera/",
 "https://mlhe2s6bvl6i.i.optimole.com/w:1385/h:900/q:auto/https://travelland.kg/wp-content/uploads/2020/02/stambul.jpg")
add_product(
 "Germany", "Tours to Germany",
 "от 793 USD, more details here-> http://putevka.kg/tours/turyi-v-germaniyu-iz-bishkeka/",
 "https://wantsee.world/wp-content/uploads/2020/05/Germany-Travel.jpg")
add_product(
 "Egypt", "Tours to Egypt",
 "от 615 USD, more details here-> http://putevka.kg/tours/egipet-rannee-bronirovanie/",
 "https://files.tpg.ua/pages2/87803/Egypt_main.jpg")
add_product(
 "France", "Tours to France",
 "от 876 USD, more details here-> http://putevka.kg/tours/turyi-v-parizh-iz-bishkeka/",
 "https://fotorelax.ru/wp-content/uploads/2016/02/Walk-around-Paris-01.jpg")
add_product(
 "Turkey", "Last Minute Hotels in Antalya",
 "от 505 USD, more details here-> http://putevka.kg/tours/goryashie-tury-v-antaliyu-2/",
 "https://i.summerhome.net/uploads/images/blog/2019/antalya-kapak.jpg")
add_product(
 "Dubai", " Tours to Dubai",
 "530 USD, more details here-> http://putevka.kg/tours/tury-v-oae-iz-bishkeka/",
 "https://i.ytimg.com/vi/GeGRBGDsSDw/maxresdefault.jpg")
add_product(
 "Czech", "Tours to Czech",
 "от 630 USD, more details here-> http://putevka.kg/tours/tury-v-chehiyu/",
 "https://content.luxe.ru/images/290755.jpg")
add_product(
 "Thailand", "Tours to Thailand",
 "от 669 USD, more details here-> https://kochevnik.kg/tours/tailand-splash-beach-resort-by-langham-5/",
 "https://happy-travel.kz/upload/images/86121_629275_16.jpg")
add_product(
 "Goa", "Tours to Goa",
 "от 515 USD, more details here-> http://putevka.kg/tours/tury-na-goa/",
 "https://34travel.me/media/upload/images/2016/october/Goa_winter/1%20(1).jpg")
add_product(
 "Sri Lanka", "Tours to Sri Lanka",
 "от 515 USD, more details here-> https://kochevnik.kg/tours/shri-lanka-citrus-waskaduwa-5/",
 "https://internationalinvestment.biz/uploads/posts/2018-02/1518249866_85b16118ed88b8d554f1ce60398dc7cf.jpg")
add_product(
 "Maldives", "Tours to Maldives",
 "от 515 USD, more details here-> https://kochevnik.kg/tours/maldivy-paradise-island-resort-5/",
 "https://otdyhateli.com/wp-content/uploads/2016/03/Extraordinary-Velassaru-Island-in-the-Maldives-54.jpg")
# Bot function

@bot.message_handler(content_types=['text'])
def bot_function(message):
    mes = message.text
    markup = get_categories_list()
    if mes == "/start":
        bot.send_message(message.from_user.id,
                         "Good day "+message.from_user.first_name)
        bot.send_message(message.from_user.id,
                         "Then you can choose a suitable trip to the proposed countries ...")
        bot.send_message(message.from_user.id,
                         "We offer trips to the proposed countries at the lowest prices")
        bot.send_message(message.from_user.id,
                         "Choose from the category, the places where you plan to visit in the near future",
                         reply_markup=markup)
    elif mes == "/spnsr":
        bot.send_message(message.from_user.id,
                         "kochevnik.kg")
        bot.send_message(message.from_user.id,
                         "putevka.kg")
    elif mes == "Помощь":
        bot.send_message(message.from_user.id,
                         "Visit_countries_bot is a bot specially for Bishkek citizens to travel." +
                         "We offer sites for finding travel deals at the best prices. " +
                         "Write or click on '/start' ," +
                         "To find out more about our partners click on /spnsr",
                         reply_markup=markup)
    elif mes in PRODUCTS:
        send_products(message.from_user.id, mes, markup)
    else:
        bot.send_message(message.from_user.id,
                         "Nothing found. Enter the correct tag",
                         reply_markup=markup)
bot.polling(none_stop=True)

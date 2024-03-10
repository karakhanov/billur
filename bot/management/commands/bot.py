import telebot
from django.core.management import BaseCommand

# client = googlemaps.Client(key='AIzaSyC7RoldSIPoNDlTWiSQzkz9diepfYzOks8')
bot_token = '6858304393:AAHupKmNEygBwbD1_D9taw4saohmGFfbQv8'

bot = telebot.TeleBot(token=bot_token)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

from bot.models import botUser

telebott = telebot.types


class Command(BaseCommand):

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        id = message.from_user.id
        firstName = message.from_user.first_name
        lastName = message.from_user.last_name
        username = message.from_user.username

        keyboard = telebott.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        buttonContact = telebott.KeyboardButton(text="Raqamni jo'natish", request_contact=True)

        welcome = ("Botdan foydalanish uchun iltimos, Telefon raqamingizni yuboring!\n"
                   "Telefon raqamingizni yuborish uchun quyidagi "'Raqamni jo`natish'" bosing 👇\n\n\n"
                   "Для пользование данным ботом, пожалуйста отправьте номер телефона\n"
                   "Для отправки номер телефона нажмите кнопку ниже 👇")
        try:
            Users = botUser(user_id=id, firstname=firstName, lastname=lastName, username=username)
            Users.save()
            keyboard.add(buttonContact)
        except Exception as e:
            print(e)
        welcome = ("Botdan foydalanish uchun iltimos, Telefon raqamingizni yuboring!\n"
                   "Telefon raqamingizni yuborish uchun quyidagi "'Raqamni jo`natish'" bosing 👇\n\n\n"
                   "Для пользование данным ботом, пожалуйста отправьте номер телефона\n"
                   "Для отправки номер телефона нажмите кнопку ниже 👇")
        bot.reply_to(message, welcome, reply_markup=keyboard)

    @bot.message_handler(content_types=['contact'])
    def contact(message):
        number = message.contact.phone_number
        keyboard = telebott.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        welcome = 'Rahmat'
        if botUser.objects.filter(user_id=message.from_user.id).filter(phone__isnull=True):
            try:
                Users = botUser.objects.filter(user_id=message.from_user.id).update(phone=number)
                print(number)
                keyboard = telebott.ReplyKeyboardRemove()
                keyboard = telebott.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                welcome = '🇺🇿 Ассалом алайкум! Илтимос тилни танланг 👇\n\n 🇷🇺 Здравствуйте! Пожалуйста выберите язык 👇'
                button_uz = telebott.KeyboardButton(text='Ўзбекча 🇺🇿')
                button_ru = telebott.KeyboardButton(text='Русский 🇷🇺')
                keyboard.add(button_ru, button_uz)
                # bot.register_next_step_handler(keyboard, on_click)
            except Exception as e:
                print(e)
        else:
            print('11')
            # print(message.location.longitude)
            # print(message)
        bot.reply_to(message, welcome, reply_markup=keyboard)
        bot.register_next_step_handler(message, message.tilTanlash)

    # @bot.message_handler(commands=['Ўзбекча 🇺🇿'])
    # def uz(message):
    #     language = 'Ўзбекча 🇺🇿'
    #     keyboard = telebott.ReplyKeyboardRemove()
    #     botUser.objects.filter(user_id=message.from_user.id).update(lang=language)
    #     ff = botUser.objects.filter(user_id=message.from_user.id).all() + '!'
    #     bot.reply_to(message, language, reply_markup=keyboard)
    #

    def tilTanlash(message):
        langUz = 'Ўзбекча 🇺🇿'
        langRu = 'Русский 🇷🇺'
        keyboard = telebott.ReplyKeyboardRemove()
        botUser.objects.filter(user_id=message.from_user.id).update(lang=language)
        ff = botUser.objects.filter(user_id=message.from_user.id).all() + '!'
        bot.reply_to(message, reply_markup=keyboard)
    # @bot.message_handler(content_type=['contact'])
    # def contact(message):
    #     number = message.from_user.

    def on_click(message):
        print("salom")
        if message.text == "Русский 🇷🇺":

            print("ru")
        elif message.text == "Ўзбекча 🇺🇿":
            print("uz")


    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()

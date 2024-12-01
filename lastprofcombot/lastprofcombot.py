from aiogram import Bot, Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7963076089:AAG2lT8P_c4qswy-hC1PixXYRr5E9r86hLY')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://ya.ru')))
    await message.answer('Привет,мой ноги!', reply_markup=markup)
    


executor.start_polling(dp)
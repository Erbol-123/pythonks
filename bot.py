from aiogram import types, Bot,executor,Dispatcher
from keyboards import

api = '7420564756:AAEcbvQcSx4JEMPP7LIC8EUblRR8iWAUZo4'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Salem')


if __name__=='__main__':
    executor.start_polling(dp,skip_ updates=True)
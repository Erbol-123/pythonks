from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

menu = KeyboardButton(text='🍽Menu🍽')
contacts = KeyboardButton(text='📱Contacts📱')



main_menu.add(menu,contacts)



from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '	\U0001F354 Katalog'

cart = '๐ Savat'
delivery_status = '๐ Buyurtma holati'

settings = 'โ๏ธKatalogni sozlash'
orders = '๐ Buyurtmalar'
questions = 'โ Savollar'

@dp.message_handler(IsAdmin(), commands='start')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Menu', reply_markup=markup)

@dp.message_handler(IsUser(), commands='start')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(questions,catalog)
    markup.add(cart)

    await message.answer('Menu', reply_markup=markup)

from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async  def set_commands(bot: Bot):
     commands = [
        types.BotCommand(command='/start', description= 'Команда для того, чтобы заупстить бота'),
        types.BotCommand(command='/help', description= 'Команда для того, чтобы узнать, с чем может помочь Бот'),
        types.BotCommand(command='/love', description='Команда для того, чтобы бота отправил стих Пушкина'),
        types.BotCommand(command='/life', description='Команда для того, чтобы бот отправил цитату'),
        types.BotCommand(command='/konfici', description='Команда для того, чтобы бот отправил слова Конфуция')
     ]

     await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый эхо бот')

@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе с...')


@dp.message_handler(commands='love')
async def start(message: types.Message):
    await message.reply('Я вас любил: любовь еще, быть может,\nВ душе моей угасла не совсем;Но пусть она вас больше не тревожит;\nЯ не хочу печалить вас ничем.\nЯ вас любил безмолвно, безнадежно,То робостью, то ревностью томим;\nЯ вас любил так искренно, так нежно\n Как дай вам Бог любимой быть другим.')


@dp.message_handler(commands='life')
async def start(message: types.Message):
    await message.reply('Жизнь - это то, что с тобой происходит, пока ты строишь планы.')

@dp.message_handler(commands='konfici')
async def start(message: types.Message):
    await message.reply('Конфуций: «Чего не желаешь себе, того не делай и другим» ')

@dp.message_handler()
async  def echo(message: types.Message):
    await message.answer(message.text)


async  def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

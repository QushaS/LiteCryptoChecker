import blockcypher
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot('5548169741:AAEfs60DEdFhEDwwZUHvRSm8fuYu0Ec_qj4', parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer('<b>Добро пожаловать!</b>\n\n<i>Введите адрес интересующего вас кошелька, а я выведу вам баланс.</i>')


@dp.message_handler()
async def check(msg: types.Message):
    try:
        balance_satoshi = blockcypher.get_total_balance(msg.text, 'btc',
                                                        'da45f1c038d8419c8aef2cd9663b4791')
        balance_btc = blockcypher.from_base_unit(balance_satoshi, 'btc')
        await msg.answer(f'Баланс:\n<b>{balance_btc} btc</b>')
    except Exception as E:
        await msg.answer(f'Похоже, вы неправильно записали адрес кошелька!')

executor.start_polling(dp)

from aiogram import Bot, Dispatcher
from config import Config, add_config
from handlers import user_handlers
import asyncio
from handbook import handbook

async def main():
    config = add_config()
    bot = Bot(token=config.telegram_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) # start polling!! а не run_polling


asyncio.run(main())
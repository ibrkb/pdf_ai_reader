import asyncio
from aiogram import Bot , Dispatcher 
from handlers.start import router as start_router
from handlers.pdf_handler import router as pdf_router 
from config import Bot_Token 
from handlers.chat import router as chat_router

async def main():
    bot = Bot(token=Bot_Token)
    dp = Dispatcher()

    

    dp.include_router(start_router)
    dp.include_router(pdf_router)
    dp.include_router(chat_router)

    print('PDF AI Bot  IS botting ...')
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

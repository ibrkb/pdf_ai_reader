from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message  

    
router = Router()

@router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(
        "👋 Welcome to PDF AI Bot!\n\n"
        "📄 Send me a PDF document.\n"
        "💬 Then ask me questions about it."
    )




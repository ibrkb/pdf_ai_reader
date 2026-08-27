from aiogram import Router , F
from aiogram.types import Message  
from services.storage import get_document
from services.llm import generate_answer
router = Router()

@router.message(F.text)
async def chat_handler(message: Message):
    document_text = get_document(message.from_user.id)

    if not document_text :
        await message.answer(
            "📄 Please send me a PDF first, then ask me a question about it."
        )
        return

    question = message.text

    await message.answer(
        f"🤔 You asked:\n{question}\n\n"
        f"📚 I found your PDF. Next, I will use AI to answer your question."
    )

    await message.answer("🤖 Thinking...")

    try :
        answer = generate_answer(question , document_text)
        await message.answer(answer)

    except Exception as error:
        print(f"AI Error: {error}")

        await message.answer(
            "❌ Sorry, I couldn't generate an answer."
        )


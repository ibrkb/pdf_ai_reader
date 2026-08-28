from aiogram import Router , F
from aiogram.types import Message  
from services.storage import get_document
from services.llm import generate_answer
from services.vector_store import search_chunks , add_chunks_to_database
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
        top_chunks = search_chunks(question, n_results=3)
        print('-----------------')
        print(top_chunks)
        print('-----------------')
        answer = generate_answer(question , top_chunks)
        await message.answer(answer)

    except Exception as error:
        print(f"AI Error: {error}")

        await message.answer(
            "❌ Sorry, I couldn't generate an answer."
        )


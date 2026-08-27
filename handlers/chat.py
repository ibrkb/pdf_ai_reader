from aiogram import Router , F
from aiogram.types import Message  
from services.storage import get_document
from services.llm import generate_answer
from embeddings import find_relevant_chunks
from services.retrieval import split_into_chunks
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
        chunks = split_into_chunks(document_text,chunk_size=500,overlap=50) 
        print('-----------------')
        print(f"Created {len(chunks)} chunks\n")
        print('-----------------')
        top_chunks = find_relevant_chunks(question, chunks, top_n=3)
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


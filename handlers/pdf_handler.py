from aiogram import Router , F 
from aiogram.filters import Command
from aiogram.types import Message  
from pathlib import Path
from services.pdf_service import extract_text
from services.storage import save_document , get_document   
from services.retrieval import split_into_chunks
from services.vector_store import add_chunks_to_database
router = Router()

data_dir = Path("data")

@router.message(F.document)
async def pdf_handler(message:Message ):
    document =message.document

    if document.mime_type != "application/pdf":
        await message.answer(
        "Sorry, I can't process this file!\n"
        "❌ Please send a PDF file."
        )
        return


    data_dir.mkdir(exist_ok=True)
    file_path = data_dir / document.file_name
    await message.bot.download(document , destination = file_path)

 
    text = extract_text(file_path)
    if not text.strip():
        await message.answer(
            "❌ I couldn't extract text from this PDF."
        )
        return
    

    save_document(message.from_user.id, text)
    chunks = split_into_chunks(text,chunk_size=500,overlap=50)

    print('-----------------')
    print(f"Created {len(chunks)} chunks\n")
    print('-----------------')

    add_chunks_to_database(
            chunks,
            source=f"user_{message.from_user.id}_document"
        )
    
    await message.answer(
        f"✅ PDF processed successfully!\n\n"
        f"📄 File: {document.file_name}\n"
        f"File size{document.file_size}\n"
        f"📊 Extracted characters: {len(text)}\n\n"
        f"💬 You can now ask me questions about this PDF!"
    )


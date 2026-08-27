import ollama 
from config import MODEL

def generate_answer(question,context):
    prompt =f"""
        You are a helpful PDF assistant.

        Answer the user's question using ONLY the information
        provided in the PDF context.

        If the answer is  not in the context, say:

        "I could not find the answer in the uploaded PDF."

        PDF CONTEXT:
        {context}

        USER QUESTION:
        {question}
        """


    response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    return response.message.content

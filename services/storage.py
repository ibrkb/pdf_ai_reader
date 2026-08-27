user_documents = {}


def save_document(user_id ,text):
    user_documents[user_id] = text


def get_document(user_id):
    return user_documents.get(user_id)






def split_into_chunks (text: str , chunk_size: int = 500 , overlap : int = 50 ):
    chunks =[]
    start = 0 
    text_len = len(text)
    while start < text_len :
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start += chunk_size - overlap
    return chunks 

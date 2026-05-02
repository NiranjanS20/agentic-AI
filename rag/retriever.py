from rag.embeddings import embed_query

def retrieve_context(vector_store, query):
    query_embedding = embed_query(query)
    results = vector_store.search(query_embedding)
    return "\n\n".join(results)

import numpy as np
from embeddings import get_embedding

_vectors = []
_texts = []

def store_documents(docs):
    for doc in docs:
        _vectors.append(np.array(get_embedding(doc)))
        _texts.append(doc)

def search(query, top_k=2):
    query_vec = np.array(get_embedding(query))

    scores = []
    for vec in _vectors:
        score = np.dot(query_vec, vec) / (
            np.linalg.norm(query_vec) * np.linalg.norm(vec)
        )
        scores.append(score)

    top_indices = np.argsort(scores)[-top_k:][::-1]
    return [_texts[i] for i in top_indices]

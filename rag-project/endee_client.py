import numpy as np

class EndeeClient:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, vector, text):
        self.vectors.append(np.array(vector))
        self.texts.append(text)

    def search(self, query_vector, top_k=2):
        query = np.array(query_vector)
        scores = []

        for v in self.vectors:
            score = np.dot(query, v) / (np.linalg.norm(query) * np.linalg.norm(v))
            scores.append(score)

        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [self.texts[i] for i in top_indices]

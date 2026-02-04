from embedder import get_embedding
from endee_client import EndeeClient

client = EndeeClient()

def load_data():
    with open("data/notes.txt", "r") as f:
        for line in f:
            vector = get_embedding(line)
            client.add(vector, line.strip())

def ask(query: str):
    query_vector = get_embedding(query)
    return client.search(query_vector)

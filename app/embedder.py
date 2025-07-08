import os
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
DB_FILE = "embeddings.pkl"

if os.path.exists(DB_FILE):
    with open(DB_FILE, "rb") as f:
        db = pickle.load(f)
else:
    db = []

def embed_chunks(chunks, doc_name):
    for chunk in chunks:
        vec = model.encode(chunk)
        db.append({"text": chunk, "embedding": vec, "doc": doc_name})
    with open(DB_FILE, "wb") as f:
        pickle.dump(db, f)

def search_similar_chunks(query, top_k=3):
    q_vec = model.encode(query)
    scored = [
        (util.cos_sim(q_vec, item["embedding"]).item(), item["text"])
        for item in db
    ]
    scored.sort(reverse=True)
    return [s[1] for s in scored[:top_k]]

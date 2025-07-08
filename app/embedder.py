import os
import pickle
from typing import Iterable

from sentence_transformers import SentenceTransformer, util

MODEL_NAME = os.environ.get("EMBEDDING_MODEL", "paraphrase-MiniLM-L6-v2")
model = SentenceTransformer(MODEL_NAME)
DB_FILE = os.path.join(os.path.dirname(__file__), "embeddings.pkl")

if os.path.exists(DB_FILE):
    with open(DB_FILE, "rb") as f:
        db: list[dict] = pickle.load(f)
else:
    db = []

def embed_chunks(chunks: Iterable[str], doc_name: str) -> None:
    """Embed and store text chunks from a document."""
    for chunk in chunks:
        vec = model.encode(chunk)
        db.append({"text": chunk, "embedding": vec, "doc": doc_name})
    with open(DB_FILE, "wb") as f:
        pickle.dump(db, f)

def search_similar_chunks(query: str, top_k: int = 3) -> list[str]:
    """Return the most similar chunks for *query*."""
    if not db:
        return []
    q_vec = model.encode(query)
    scored = [
        (util.cos_sim(q_vec, item["embedding"]).item(), item["text"])
        for item in db
    ]
    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]

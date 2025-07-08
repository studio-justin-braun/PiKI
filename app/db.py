import json
import os

DOC_FILE = "db_docs.json"
CHAT_FILE = "db_chats.json"
FEEDBACK_FILE = "db_feedback.json"

def _load(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

def _save(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def save_document(name, chunks):
    data = _load(DOC_FILE)
    data.append({"name": name, "chunks": chunks})
    _save(DOC_FILE, data)

def save_chat(q, a):
    data = _load(CHAT_FILE)
    data.append({"question": q, "answer": a})
    _save(CHAT_FILE, data)

def load_chat_history():
    return _load(CHAT_FILE)

def save_feedback(q, a, fb):
    data = _load(FEEDBACK_FILE)
    data.append({"question": q, "answer": a, "feedback": fb})
    _save(FEEDBACK_FILE, data)

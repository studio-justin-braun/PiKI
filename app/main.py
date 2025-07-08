from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

from llm_runner import generate_answer
from embedder import embed_chunks, search_similar_chunks
from processor import process_document
import db

app = Flask(__name__)
chat_history: list[dict] = []
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    context = "\n".join(search_similar_chunks(user_input))
    response = generate_answer(user_input, context=context)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "ai", "content": response})
    db.save_chat(user_input, response)
    return jsonify({"response": response})


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file"}), 400
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    chunks = process_document(path)
    embed_chunks(chunks, filename)
    db.save_document(filename, chunks)
    return jsonify({"status": "ok", "chunks": len(chunks)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

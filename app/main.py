from flask import Flask, render_template, request, jsonify
from llm_runner import generate_answer

app = Flask(__name__)
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = generate_answer(user_input)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "ai", "content": response})
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

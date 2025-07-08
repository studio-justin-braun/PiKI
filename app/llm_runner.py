import subprocess

def generate_answer(question):
    prompt = f"<|user|>\n{question}\n<|assistant|>"

    result = subprocess.run([
        "/home/pi/piki/llama.cpp/build/bin/llama-cli",
        "-m", "/home/pi/piki/llama.cpp/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "-p", prompt,
        "--n-predict", "128",
        "--chat-template", "",
        "--prompt-cache", "false"
    ], capture_output=True, text=True)

    print("PROMPT:", prompt)
    print("ANTWORT:", result.stdout)
    print("FEHLER:", result.stderr)

    return result.stdout.strip()

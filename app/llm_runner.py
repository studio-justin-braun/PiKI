import os
import subprocess

LLAMA_CLI = os.environ.get("LLAMA_CLI", "/home/pi/piki/llama.cpp/build/bin/llama-cli")
MODEL_FILE = os.environ.get(
    "LLAMA_MODEL",
    "/home/pi/piki/llama.cpp/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
)


def _call_llama(prompt: str) -> str:
    """Call the llama.cpp binary if available."""
    if not os.path.exists(LLAMA_CLI):
        raise FileNotFoundError(LLAMA_CLI)

    result = subprocess.run(
        [
            LLAMA_CLI,
            "-m",
            MODEL_FILE,
            "-p",
            prompt,
            "--n-predict",
            "128",
            "--chat-template",
            "",
            "--prompt-cache",
            "false",
        ],
        capture_output=True,
        text=True,
    )

    return result.stdout.strip()


def generate_answer(question: str, context: str | None = None) -> str:
    """Generate an answer for *question* optionally using extra *context*."""
    prompt_parts = []
    if context:
        prompt_parts.append(context)
    prompt_parts.append(question)
    prompt = "\n".join(prompt_parts)
    prompt = f"<|user|>\n{prompt}\n<|assistant|>"

    try:
        return _call_llama(prompt)
    except FileNotFoundError:
        # Fallback for environments without llama.cpp
        return f"(Simulierte Antwort) {question}"

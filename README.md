# PiKI Chatbot

Dieses Projekt stellt einen einfachen lokalen Chatbot bereit. Neben normalen Chatnachrichten können PDF-Dokumente hochgeladen und anschließend in Fragen einbezogen werden.

## Installation

1. Abhängigkeiten installieren:
   ```bash
   pip install flask pdfplumber sentence-transformers
   ```
2. Anwendung starten:
   ```bash
   python3 app/main.py
   ```

Optional kann `LLAMA_CLI` und `LLAMA_MODEL` auf eine installierte `llama.cpp`-Binary bzw. ein Modell gesetzt werden. Ist keine Binary vorhanden, wird eine Platzhalterantwort generiert.

## Nutzung

- Im Browser `http://localhost:5000` aufrufen.
- Über das Formular können PDF-Dateien hochgeladen werden.
- Anschließend Fragen im Chat stellen. Der Chat nutzt relevante Ausschnitte der hochgeladenen Dokumente als Kontext.

Alle Chats und Dokumente werden lokal in JSON- und Pickle-Dateien abgelegt.

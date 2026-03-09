AI Voice Interview Assistant

A real-time AI interview assistant that listens to spoken questions, converts speech to text, generates answers using an LLM, and displays responses in a floating overlay window.

This project demonstrates how to combine speech recognition, local LLMs, and a lightweight UI to build an AI-powered interview helper.

Features

🎤 Voice Input – Capture interview questions using the microphone

🧠 AI Response Generation – Generate answers using a local LLM

⚡ Fast Speech Recognition – Powered by Faster Whisper

🪟 Floating Overlay UI – Always-on-top assistant window

🔄 Continuous Listening – Automatically processes questions in a loop

💻 Fully Local Execution – No external API required

Architecture
Microphone
   ↓
Speech Recognition (Faster Whisper)
   ↓
Question Text
   ↓
Local LLM (via Ollama)
   ↓
Generated Answer
   ↓
Overlay UI
Technologies Used

Python

Faster Whisper – Speech-to-text

Ollama – Local LLM runtime

TinyLlama – Fast lightweight language model

Tkinter – Overlay UI

SoundDevice – Audio capture

Project Structure
parakeet-fast
│
├ main.py
├ speech_engine.py
├ llm_engine.py
├ overlay_ui.py
└ audio
Installation
1. Clone the repository
git clone https://github.com/your-username/interview-ai-assistant.git
cd interview-ai-assistant
2. Install dependencies
pip install faster-whisper sounddevice numpy scipy requests
3. Install Ollama

Install Ollama from:

https://ollama.com

Download the fast model:

ollama pull tinyllama
Running the Assistant

Start Ollama:

ollama run tinyllama

Run the assistant:

python main.py

The assistant will:

Listen for voice input

Convert speech to text

Generate an answer using the LLM

Display the answer in a floating overlay window

Example
Question: What is Python OOP?

Answer:
Object-oriented programming in Python is a paradigm based on classes and objects. 
It allows encapsulation, inheritance, and polymorphism.
Performance

Typical response time:

Step	Time
Speech recognition	~300-500 ms
LLM generation	~1-2 s
Total response	~1-2.5 s
Limitations

Local LLMs may produce slower responses compared to cloud APIs

Speech recognition accuracy depends on microphone quality

Coding interview answers may require larger models

Future Improvements

Streaming speech recognition

Real-time response generation

Support for coding interview assistance

Resume-aware responses (RAG)

Screen text detection for coding problems

License

MIT License

Author

Vaibhav Desai

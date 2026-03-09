import threading
from speech_engine import record_audio, transcribe
from llm_engine import ask_llm
from overlay_ui import Overlay

ui = Overlay()

print("AI Assistant Started")


def process_audio():

    audio_file = record_audio()

    question = transcribe(audio_file)

    if question == "":
        return

    print("Question:", question)

    ui.update("Question:\n" + question)

    answer = ask_llm(question)

    print("Answer:", answer)

    ui.update("Answer:\n" + answer)


def audio_loop():

    while True:
        process_audio()


threading.Thread(target=audio_loop, daemon=True).start()

ui.run()
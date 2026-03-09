import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import os

# FAST MODEL
model = WhisperModel("tiny", compute_type="int8")

def record_audio(filename="audio/question.wav", duration=2, fs=16000):

    os.makedirs("audio", exist_ok=True)

    print("Listening...")

    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, fs, audio)

    return filename


def transcribe(file):

    segments, info = model.transcribe(file, beam_size=2)

    text = ""

    for seg in segments:
        text += seg.text

    return text.strip()
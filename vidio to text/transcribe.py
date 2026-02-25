import whisper
import os

# Load the base model (you can use "small", "medium", or "large" for better accuracy)
model = whisper.load_model("base")

# File path
audio_file = "myvideo.m4a"

# Ensure file exists
if not os.path.exists(audio_file):
    raise FileNotFoundError(f"Audio file not found: {audio_file}")

# Transcribe the audio (specify language to help accuracy)
result = model.transcribe(audio_file, language="ar")  # "ar" for Arabic

# Print transcription
print(result["text"])

# Save to file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

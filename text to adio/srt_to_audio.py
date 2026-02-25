import pysrt
from gtts import gTTS
from pydub import AudioSegment
import os

# === CONFIG ===
SRT_FILE = 'subtitles.srt'
OUTPUT_DIR = 'output_audio'
LANGUAGE = 'en'  # Change to 'en' for English
COMBINE_ALL = True  # Set to False if you don't want a single output file

# === PREPARE ===
os.makedirs(OUTPUT_DIR, exist_ok=True)
subs = pysrt.open(SRT_FILE)
combined_audio = AudioSegment.empty()

# === PROCESS EACH SUBTITLE LINE ===
for index, sub in enumerate(subs):
    text = sub.text.strip().replace('\n', ' ')
    if not text:
        continue  # Skip empty subtitles

    print(f"🔊 Processing line {index}: {text}")

    try:
        # Calculate duration in ms
        start = sub.start.to_time()
        end = sub.end.to_time()
        duration_ms = (
            (end.hour - start.hour) * 3600000 +
            (end.minute - start.minute) * 60000 +
            (end.second - start.second) * 1000 +
            (end.microsecond - start.microsecond) // 1000
        )

        # Generate speech
        tts = gTTS(text=text, lang=LANGUAGE)
        temp_path = os.path.join(OUTPUT_DIR, f"temp_{index}.mp3")
        tts.save(temp_path)

        # Load and adjust audio
        audio = AudioSegment.from_mp3(temp_path)
        os.remove(temp_path)  # Clean up temp file

        if len(audio) < duration_ms:
            silence = AudioSegment.silent(duration=duration_ms - len(audio))
            audio += silence
        else:
            audio = audio[:duration_ms]

        # Export adjusted audio
        final_path = os.path.join(OUTPUT_DIR, f"line_{index:03d}.mp3")
        audio.export(final_path, format="mp3")

        # Combine if needed
        if COMBINE_ALL:
            combined_audio += audio

    except Exception as e:
        print(f"❌ Error processing line {index}: {e}")
        continue

# === EXPORT COMBINED AUDIO ===
if COMBINE_ALL and len(combined_audio) > 0:
    combined_path = os.path.join(OUTPUT_DIR, 'final_combined.mp3')
    combined_audio.export(combined_path, format="mp3")
    print(f"✅ Combined audio exported to {combined_path}")

print("🎉 Done: All audio segments processed.")

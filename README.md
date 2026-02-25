# text-to-audio-video-to-text-
text to audio, video to text simple python project
text to audio :
 this is a srt text to audio. requirements py libraries like: 
  import pysrt
  from gtts import gTTS
  from pydub import AudioSegment
  import os
 # === CONFIG ===
SRT_FILE = 'subtitles.srt' #in same folder
OUTPUT_DIR = 'output_audio'
LANGUAGE = 'en'  # Change to 'en' for English
COMBINE_ALL = True  # Set to False if you don't want a single output file
video to text:
this is a video to tex. requirements py libraries like: 
  import whisper
  import os
 # Load the base model (you can use "small", "medium", or "large" for better accuracy)
model = whisper.load_model("base")
# File path in same folder 
audio_file = "myvideo.m4a"
# Transcribe the audio (specify language to help accuracy)
result = model.transcribe(audio_file, language="en")  # "en" for ENGLISH


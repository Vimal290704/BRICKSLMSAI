import os
from io import BytesIO
from dotenv import load_dotenv #type: ignore
from elevenlabs.client import ElevenLabs #type: ignore
import time
load_dotenv()
global text , transcribe_start , transcribe_end , speech_start , speech_end
client = ElevenLabs(api_key=os.getenv("ELEVENLAB_API_KEY"))

voices = client.voices.get_all()
print(voices.json())
# audio_path = "./English-recording.wav"

# with open(audio_path, "rb") as f:
#     audio_data = f.read()
#     transcribe_start = time.time()
#     response = client.speech_to_text.convert(
#         file = BytesIO(audio_data),
#         model_id="scribe_v1",  
#     )
#     text = response.text
#     transcribe_end = time.time()

# print(text)

# speech_start = time.time()

# speech = client.text_to_speech.convert(
#     voice_id="CwhRBWXzGAHq8TQ4Fs17",
#     output_format="mp3_44100_128",
#     text=text,
# )

# speech_bytes = b''

# for chunk in speech:
#     speech_bytes += chunk

# with open("speech.mp3" , "wb") as f:
#     f.write(speech_bytes)

# speech_end = time.time()

# print(f"Time taken for transcribtion : {transcribe_end - transcribe_start}") 
# print(f"Time taken for speech : {speech_end - speech_start}") 
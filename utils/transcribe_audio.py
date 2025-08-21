# import whisper

# model = whisper.load_model("base")  # or "small", "medium"

# def transcribe_audio(audio_path):
#     print(f"[DEBUG] Transcribing from: {audio_path}")
#     result = model.transcribe(audio_path)
#     return result["text"]

# import whisper

# model = whisper.load_model("base")

# def transcribe_audio(audio_path):
#     result = model.transcribe(audio_path)
#     return result['text']
import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    print(f"[DEBUG] Transcribing from: {audio_path}")
    try:
        result = model.transcribe(audio_path, language='kn', task='translate')
        print(f"[SUCCESS] Transcription result:\n{result['text']}")
        return result["text"]
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        return None

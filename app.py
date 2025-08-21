# import os
# import torch
# from utils.extract_audio import extract_audio_from_video
# from utils.transcribe_audio import transcribe_audio

# def process_video(video_path):
#     print(f"[INFO] Processing video: {video_path}")

#     # Extract filename for naming audio/transcript
#     filename = os.path.splitext(os.path.basename(video_path))[0]

#     audio_path = os.path.join("audio_output", f"{filename}.wav")
#     print(f"[INFO] Audio will be saved to: {audio_path}")

#     # Extract audio
#     extract_audio_from_video(video_path, audio_path)
#     print(f"[SUCCESS] Audio extracted to: {audio_path}")

#     # Transcribe audio
#     print("[INFO] Transcribing audio...")
#     transcript = transcribe_audio(audio_path)

#     if transcript:
#         print("\n📄 TRANSCRIPT 📄\n")
#         print(transcript)

#         # Save transcript
#         os.makedirs("transcript", exist_ok=True)
#         transcript_path = os.path.join("transcript", f"{filename}.txt")
#         with open(transcript_path, "w", encoding="utf-8") as f:
#             f.write(transcript)

#         print(f"\n[SAVED] Transcript saved to: {transcript_path}")
#     else:
#         print("[ERROR] Transcription failed or empty result.")

# if __name__ == "__main__":
#     # Optional: change video file name if needed
#     video = "video_input/video1.mp4"

#     # Set device to CPU (or change to "cuda" if GPU is available)
#     device = "cuda" if torch.cuda.is_available() else "cpu"
#     print(f"Device set to use {device}")

#     process_video(video)

import os
import sys
import torch
from utils.extract_audio import extract_audio_from_video
from utils.transcribe_audio import transcribe_audio

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device set to use {device}")

# Get video filename from command-line argument
if len(sys.argv) < 2:
    print("Usage: python app.py <video_filename>")
    sys.exit(1)

video_filename = sys.argv[1]
video_path = os.path.join("video_input", video_filename)

# Define output paths
audio_output_path = os.path.join("audio_output", video_filename.replace(".mp4", ".wav"))
transcript_output_path = os.path.join("transcripts", video_filename.replace(".mp4", ".txt"))

print(f"[INFO] Processing video: {video_path}")
print(f"[INFO] Audio will be saved to: {audio_output_path}")

# Step 1: Extract Audio
extract_audio_from_video(video_path, audio_output_path)

# Step 2: Transcribe Audio
print("[INFO] Transcribing audio...")
transcript = transcribe_audio(audio_output_path)

if transcript:
    print("[SUCCESS] Transcription Complete!\n")
    print(transcript)

    # Save to transcript file
    os.makedirs("transcripts", exist_ok=True)
    with open(transcript_output_path, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"[INFO] Transcript saved to {transcript_output_path}")
else:
    print("[ERROR] No transcript generated.")

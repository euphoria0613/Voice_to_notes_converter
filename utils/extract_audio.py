from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio_path)

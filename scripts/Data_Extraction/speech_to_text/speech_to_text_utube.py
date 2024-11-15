import yt_dlp
import moviepy.editor as mp
import whisper
import os
import argparse

# Function to download audio from a YouTube video
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'audio.wav'

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    # Load the Whisper model (choose from "tiny", "base", "small", "medium", or "large")
    model = whisper.load_model("base")
    
    # Transcribe the audio file
    result = model.transcribe(audio_file)
    
    return result['text']

# Main function
def main(url):
    print("Downloading audio from YouTube...")
    audio_file = download_audio(url)
    
    if os.path.exists(audio_file):
        print("Transcribing audio...")
        transcription = transcribe_audio(audio_file)
        
        # Save the transcription to a text file
        with open("transcription.txt", "w") as f:
            f.write("Transcription:\n")
            f.write(transcription)
        
        print("Transcription completed! Saved to 'transcription.txt'")
        
        # Clean up the audio file
        os.remove(audio_file)
    else:
        print("Failed to download the audio.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Shorts Transcription")
    parser.add_argument("url", help="URL of the YouTube video to transcribe")
    args = parser.parse_args()
    main(args.url)

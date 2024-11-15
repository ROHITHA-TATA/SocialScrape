import instaloader
import moviepy.editor as mp
import os
import whisper
import argparse
import shutil  # Import shutil to delete the reel folder

# Function to download Instagram Reel
def download_reel(url):
    try:
        loader = instaloader.Instaloader()
        # Create the 'reel' directory if it doesn't exist
        os.makedirs('reel', exist_ok=True)
        loader.download_post(instaloader.Post.from_shortcode(loader.context, url.split('/')[-2]), target='reel')
        video_file = [f for f in os.listdir('reel') if f.endswith('.mp4')][0]
        return os.path.join('reel', video_file)
    except Exception as e:
        print(f"Error downloading reel: {e}")
        return None

# Function to convert video to audio
def convert_video_to_audio(video_file):
    clip = mp.VideoFileClip(video_file)
    clip.audio.write_audiofile("audio.wav")
    return "audio.wav"

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    # Load the Whisper model (choose from "tiny", "base", "small", "medium", or "large")
    model = whisper.load_model("base")
    
    # Transcribe the audio file
    result = model.transcribe(audio_file)
    
    return result

# Main function
def main(url):
    print("Downloading Reel...")
    video_file = download_reel(url)
    
    if video_file:
        print("Converting video to audio...")
        audio_file = convert_video_to_audio(video_file)
        
        print("Transcribing audio...")
        transcript = transcribe_audio(audio_file)
        
        if transcript:
            print("Transcription Completed!")
            
            # Save transcript to file
            with open("transcription.txt", "w") as f:
                f.write("Full Transcript:\n")
                f.write(transcript['text'] + "\n\n")
                
            print("Transcription saved to 'transcription.txt'")
        
        # Clean up files
        os.remove(audio_file)  # Delete the audio file
        shutil.rmtree('reel')  # Delete the entire 'reel' folder and its contents
        print("Reel files deleted after transcription.")
    else:
        print("Failed to download the reel.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Reel Transcription")
    parser.add_argument("url", help="URL of the Instagram Reel to transcribe")
    args = parser.parse_args()
    main(args.url)

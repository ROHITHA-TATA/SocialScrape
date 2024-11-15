# TrendScribe

This project is a Python-based tool for fetching content from YouTube and Facebook, specifically designed to retrieve details about channel videos and user posts, including comments and descriptions. The purpose of this tool is to enable content creators to easily gather structured data from their online profiles.

## Features
**YouTube Content Fetching**: Retrieves a list of videos from a specified YouTube channel, including video titles, descriptions, and URLs.  

**Facebook Content Fetching**: Fetches user information and media content (like posts and comments) from a specified Facebook account.
## Prerequisites
To Run This Project, You’ll Need:
Python 3.x  

YouTube Data API Key: Required to fetch data from YouTube.  

Facebook Graph API Access Token: Required to fetch data from Facebook. Instructions on obtaining this are also in the Setup section.  

## Python Libraries:
requests: For making HTTP requests to the APIs.  

python-dotenv: For managing environment variables securely.  

instaloader: For downloading media from Instagram, including images, videos, and metadata.  

moviepy: For handling video-to-audio conversion, specifically for extracting audio from Instagram videos.  

whisper: For transcribing audio to text. Whisper AI is used to convert the audio extracted from Instagram videos into text.  


os: For interacting with the operating system, such as file path management.  

shutil: For file operations, including moving and removing files after processing.  

argparse: For parsing command-line arguments, allowing users to input parameters directly from the command line.


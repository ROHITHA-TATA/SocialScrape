# SocialScrape

SocialScrape is a Python-based tool for fetching content from YouTube and Facebook, specifically designed to retrieve details about channel videos and user posts, including comments and descriptions. This tool enables content creators to easily gather structured data from their online profiles.

## Features

### YouTube Content Fetching
- Retrieves a list of videos from a specified YouTube channel.
- Fetches video titles, descriptions, and URLs.

### Facebook Content Fetching
- Extracts user information and media content (such as posts and comments) from a specified Facebook account.

## Prerequisites

Before running this project, ensure you have the following:

### System Requirements
- Python 3.x installed on your machine.

### API Keys & Tokens
- **YouTube Data API Key**: Required to fetch data from YouTube.
- **Facebook Graph API Access Token**: Required to fetch data from Facebook.

Instructions for obtaining these keys can be found in the **Setup** section.

### Required Python Libraries
Install the dependencies using the following command:

```bash
pip install requests python-dotenv instaloader moviepy openai whisper os shutil argparse
```

- `requests`: For making HTTP requests to APIs.
- `python-dotenv`: For managing environment variables securely.
- `instaloader`: For downloading media from Instagram, including images, videos, and metadata.
- `moviepy`: For handling video-to-audio conversion, specifically for extracting audio from Instagram videos.
- `whisper`: For transcribing audio to text (Whisper AI is used to convert extracted audio into text).
- `os`: For interacting with the operating system, such as file path management.
- `shutil`: For file operations like moving and removing files after processing.
- `argparse`: For parsing command-line arguments, allowing users to input parameters directly from the command line.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SocialScrape.git
   cd SocialScrape
   ```

2. Create a `.env` file and add your API keys:
   ```plaintext
   YOUTUBE_API_KEY=your_youtube_api_key
   FACEBOOK_ACCESS_TOKEN=your_facebook_access_token
   ```

3. Run the script with appropriate arguments:
   ```bash
   python main.py --platform youtube --channel_id YOUR_CHANNEL_ID
   ```
   ```bash
   python main.py --platform facebook --user_id YOUR_USER_ID
   ```

## Usage

- **YouTube Fetching:**
  ```bash
  python main.py --platform youtube --channel_id UC1234567890ABC
  ```

- **Facebook Fetching:**
  ```bash
  python main.py --platform facebook --user_id 123456789
  ```

## Contributing
If you’d like to contribute to SocialScrape, feel free to fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

## Contact
For any issues or suggestions, feel free to reach out or open an issue on GitHub.

---

Enjoy using **SocialScrape**!



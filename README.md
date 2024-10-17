# YouTube Video Summarizer with Translation and Annotations

This is a web-based application built using **Streamlit** that extracts transcripts from YouTube videos, generates detailed summaries using **Google Generative AI**, and translates the summary into a selected language. Additionally, the app provides functionalities like adding multimedia annotations, timestamp markers, and audio-visual customization controls for enhanced video interaction.

## Features

- **YouTube Transcript Extraction:** Fetches transcripts from YouTube videos using the video URL.
- **Summarization:** Uses Google's **Generative AI (Gemini-Pro)** to summarize the video transcript in under 500 words.
- **Translation:** Translates the summary into any desired language using **Google Translator**.
- **Annotations and Customizations:**
  - Add timestamp markers to key moments in the video.
  - Multimedia annotations (text, sound, and image).
  - Audio controls like background noise reduction and voice amplification.
  - Visual adjustment tools such as background blur.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
1. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
1. Create a `.env` file in the project directory and add your Google API key:
   ```bash
   GOOGLE_API_KEY=your_google_api_key
   ```
## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
1.  Open the browser and go to `http://localhost:8501`.
2.  Enter a valid YouTube video link and choose the target language for translation.
3.  Click the Get Detailed Notes button to generate a summary and translate it.
4.  Use additional features like timestamp markers, audio controls, and multimedia annotations to enhance the video content.
## File Overview
- `app.py`: Main Streamlit application file containing UI, transcript extraction, summarization, translation, and additional multimedia features.
- `requirements.txt`: Lists all required Python libraries.
- `.env`: Stores sensitive environment variables like the Google API key (this file should be created locally and not uploaded to GitHub).
## Dependencies
The following Python libraries are used in this project:
- `streamlit`: Web application framework to build interactive UI.
- `youtube_transcript_api`: Fetches transcripts from YouTube videos.
- `deep_translator`: Provides translation functionality.
- `googletrans`: Google Translator API.
- `google-generativeai`: Google API for generating AI-based content.
- `python-dotenv`: Manages environment variables.
## FAQs
Q1: Does this app work with all YouTube videos?
A: It works only with YouTube videos that have available transcripts (closed captions). If no transcript is available, the app will show an error.

Q2: Can I summarize videos in any language?
A: Yes, the app extracts and summarizes transcripts in any language, and you can also translate the summary into your preferred language.

Q3: How do I fix the "Quota exceeded" error?
A: Google APIs, including Generative AI, have usage quotas. If you exceed the quota, either wait for it to reset or consider upgrading your API usage plan.
## Future Improvements/To-Do
- Support for processing longer videos and large transcripts.
- Additional customization options for annotations (colors, fonts, etc.).
- Export notes and annotations to different file formats (PDF, DOCX, etc.).
- Integration with more AI models for enhanced summarization.
## License
This project is licensed under the MIT License. 
## Contributions
Contributions, issues, and feature requests are welcome! Feel free to check the issues page for open issues.
Just replace `your-username` and `your-repo-name` with your actual GitHub details!

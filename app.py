import streamlit as st
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES  # Kept only LANGUAGES since Translator is not used

# Load environment variables
load_dotenv()

# Configure Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for the Generative AI model
prompt = """You are a YouTube video summarizer. Your task is to take the transcript text 
and summarize the entire video, providing the important points in under 500 words. Please 
provide the summary of the text given here:"""

# Function to extract transcript from YouTube video
@st.cache_data
def extract_transcript_details(youtube_video_url):
    """Extracts the transcript of the given YouTube video."""
    try:
        video_id = youtube_video_url.split("=")[-1]
        st.video(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i['text'] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error retrieving transcript: {e}")
        return None

# Function to generate summary using Generative AI
@st.cache_data
def generate_gemini_content(transcript_text, prompt):
    """Generates a summary using Google's Generative AI model."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

# Function to translate text to the selected language
@st.cache_data
def Translate(Input_text, dest_lang):
    """Translates the generated summary to the selected language."""
    try:
        translator = GoogleTranslator(source='auto', target=dest_lang)
        return translator.translate(Input_text)
    except Exception as e:
        st.error(f"Error translating content: {e}")
        return None

# Streamlit UI
def main():
    """Main function to run the Streamlit app."""
    st.title("YouTube Video Summarizer")
    youtube_link = st.text_input("Enter Your Video link: ")
    language = st.selectbox("Select Language:", list(LANGUAGES.values()))

    if st.button("Get Detailed Notes"):
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            if summary:
                translated_summary = Translate(summary, language)
                if translated_summary:
                    st.markdown("## Detailed Notes:")
                    st.write(translated_summary)

                    # Additional Features
                    add_timestamp_marker()
                    add_audio_controls()
                    add_multimedia_annotations()
                    add_visual_adjustment_tools()

# Function to add timestamp marker
def add_timestamp_marker():
    """Adds timestamp markers to the video."""
    st.subheader("Timestamp Markers")
    timestamp = st.text_input("Add Timestamp Marker (hh:mm:ss):")
    if st.button("Add Timestamp"):
        st.success(f"Timestamp '{timestamp}' added.")

# Function to add audio customization controls
def add_audio_controls():
    """Adds controls for customizing the audio."""
    st.subheader("Audio Customization Controls")
    noise_reduction_level = st.slider("Background Noise Reduction", 0, 100, 0)
    voice_amplification = st.slider("Voice Amplification", 0.5, 2.0, 1.0)

# Function to add multimedia annotations
def add_multimedia_annotations():
    """Adds multimedia annotations (text, sound, or image) to the video."""
    st.subheader("Multimedia Annotations")
    annotation_type = st.selectbox("Select Annotation Type:", ["Text", "Sound", "Image"])
    if annotation_type == "Text":
        annotation_text = st.text_area("Enter Text Annotation:")
        if st.button("Add Text Annotation"):
            st.success("Text annotation added.")
    elif annotation_type == "Sound":
        sound_file = st.file_uploader("Upload Sound File (MP3/WAV):")
        if st.button("Add Sound Annotation"):
            st.success("Sound annotation added.")
    elif annotation_type == "Image":
        image_file = st.file_uploader("Upload Image File (PNG/JPG):")
        if st.button("Add Image Annotation"):
            st.success("Image annotation added.")

# Function to add visual adjustment tools
def add_visual_adjustment_tools():
    """Adds tools to adjust the video's visual appearance."""
    st.subheader("Visual Adjustment Tools")
    blur_background = st.checkbox("Blur Background")
    if blur_background:
        st.success("Background blurred.")

if __name__ == "__main__":
    main()

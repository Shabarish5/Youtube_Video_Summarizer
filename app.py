import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

load_dotenv()  # load all the environment variables

# Set Perplexity AI API key from environment variable
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# Create OpenAI client configured for Perplexity API
client = OpenAI(
    api_key=PERPLEXITY_API_KEY,
    base_url="https://api.perplexity.ai"
)

prompt = """## Goal
Create a comprehensive, detailed explanation of a YouTube video that provides valuable insights, technical understanding, and practical knowledge for viewers, focusing on clarity, depth, and accessibility.

## Return Format
1. Video Overview
   - Title and basic context
   - Main topic and purpose

2. Detailed Breakdown
   - Bulleted list of key points
   - Technical terms with simplified explanations
   - Complex terminology with precise definitions

3. Comprehensive Analysis
   - Key takeaways
   - Significant insights
   - Practical applications

4. Potential Q&A Section
   - Anticipated questions viewers might have
   - Detailed, clear answers
   - Reference timestamps from the video

## Warnings
- Avoid personal opinions
- Maintain objectivity
- Ensure accuracy of information
- Do not fabricate information not present in the video
- If a concept is unclear, explicitly state that

## Context
- Use simple, accessible language
- Explain technical terms thoroughly
- Provide context for complex concepts
- Focus on making the explanation universally understandable
- Prioritize educational value and clarity

## Additional Instructions:
- Break down complex ideas into digestible segments
- Use analogies to explain difficult concepts
- Highlight the most important information
- Ensure the explanation is comprehensive yet concise"""


# getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]
        yt_api = YouTubeTranscriptApi()
        transcript_list = yt_api.list(video_id)
        transcript = transcript_list.find_transcript(['en'])
        transcript_data = transcript.fetch()
        transcript_text = ""
        for snippet in transcript_data.snippets:
            transcript_text += " " + snippet.text
        return transcript_text
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None


# getting the summary using Perplexity AI API
def generate_summary_content(transcript_text, prompt):
    try:
        # Combine prompt with transcript text
        full_prompt = prompt + transcript_text
        
        # Generate content using Perplexity API
        response = client.chat.completions.create(
            model="sonar",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts."},
                {"role": "user", "content": full_prompt}
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating content with Perplexity API: {str(e)}"


# Sidebar with About Me section
with st.sidebar:
    st.markdown("<h2 style='color: #4B8BBE;'>📋 About Me</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size: 16px;'>
      <p><strong>👤 Name:</strong> Shabarish B L</p>
      <p><strong>🐱 GitHub:</strong> <a href='https://github.com/Shabarish5' target='_blank'>https://github.com/Shabarish5</a></p>
      <p><strong>🔗 LinkedIn:</strong> <a href='https://www.linkedin.com/in/shabarish-gowda-039358262' target='_blank'>https://www.linkedin.com/in/shabarish-gowda-039358262</a></p>
      <p><strong>📝 Profile Summary:</strong></p>
      <ul>
        <li>Experienced AI and ML Enthusiast with strong academic background</li>
        <li>Data Science Engineering Intern with practical experience in innovative solutions</li>
        <li>Created emotion detection and attendance marking system (AIEmosense)</li>
        <li>Developed personalized voice assistant using natural language processing</li>
        <li>Contributed to crime detection system using ML and computer vision</li>
        <li>Bachelor's degree in Artificial Intelligence and Machine Learning</li>
        <li>Certifications from IBM and Microsoft Azure</li>
        <li>Strong problem-solving skills and in-depth ML algorithm knowledge</li>
        <li>Eager to drive innovation in dynamic AI/ML environments</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🎬 YouTube Transcript to Detailed Notes Converter 📝</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>✨ Transform YouTube videos into comprehensive notes with AI-powered summarization ✨</p>", unsafe_allow_html=True)

youtube_link = st.text_input("🔗 Enter YouTube Video Link:", placeholder="Paste YouTube video URL here")

if youtube_link:
    try:
        video_id = youtube_link.split("v=")[1].split("&")[0]
        print(video_id)
        st.markdown(
            """
            <style>
            div[data-testid="stImage"] > img {
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", width=800, caption="📺 Video Thumbnail", use_container_width=False, clamp=False)
    except:
        st.warning("⚠️ Please enter a valid YouTube URL")

if st.button("🚀 Get Detailed Notes", type="primary"):
    with st.spinner("⏳ Processing video transcript and generating notes..."):
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_summary_content(transcript_text, prompt)
            st.markdown("<h2 style='color: #306998;'>📋 Detailed Notes:</h2>", unsafe_allow_html=True)
            st.success("✅ Notes generated successfully!")
            st.write(summary)
        else:
            st.error("❌ Could not extract transcript from this video")

# YouTube Transcript to Detailed Notes Converter 🎬📝

A powerful Streamlit web application that transforms YouTube video transcripts into comprehensive, detailed notes using AI-powered summarization with Perplexity AI.

## ✨ Features

- **YouTube Transcript Extraction**: Automatically extracts transcripts from YouTube videos
- **AI-Powered Summarization**: Uses Perplexity AI to generate detailed, structured notes
- **Comprehensive Output**: Creates organized notes with:
  - Video overview and context
  - Detailed breakdown of key points
  - Technical term explanations
  - Comprehensive analysis and insights
  - Potential Q&A section with timestamps
- **User-Friendly Interface**: Clean, intuitive Streamlit interface with video thumbnail display
- **Professional Formatting**: Well-structured output with clear sections and formatting

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Perplexity AI API key

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Perplexity AI API key:
     ```
     PERPLEXITY_API_KEY=your_api_key_here
     ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📋 Usage

1. **Enter YouTube URL**: Paste any YouTube video link in the input field
2. **View Thumbnail**: The app automatically displays the video thumbnail
3. **Generate Notes**: Click the "Get Detailed Notes" button
4. **Review Results**: The AI will process the transcript and generate comprehensive notes including:
   - Video overview and context
   - Detailed breakdown with bullet points
   - Technical explanations
   - Key insights and takeaways
   - Potential Q&A section

## 🛠️ Technical Details

### Dependencies

- `streamlit`: Web application framework
- `youtube_transcript_api`: YouTube transcript extraction
- `python-dotenv`: Environment variable management
- `openai`: Perplexity AI API integration (using OpenAI client)

### API Integration

The application uses Perplexity AI's API through the OpenAI client with the following configuration:
- Base URL: `https://api.perplexity.ai`
- Model: `sonar`
- Custom prompt engineering for comprehensive note generation

### Project Structure

```
YTS/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
PERPLEXITY_API_KEY=your_perplexity_api_key_here
```

### Customizing the Prompt

The prompt template in `app.py` can be modified to change the output format or add specific requirements for the generated notes.

## 📝 Output Format

The generated notes follow this structured format:

1. **Video Overview**
   - Title and basic context
   - Main topic and purpose

2. **Detailed Breakdown**
   - Bulleted list of key points
   - Technical terms with simplified explanations
   - Complex terminology with precise definitions

3. **Comprehensive Analysis**
   - Key takeaways
   - Significant insights
   - Practical applications

4. **Potential Q&A Section**
   - Anticipated questions viewers might have
   - Detailed, clear answers
   - Reference timestamps from the video

## ⚠️ Limitations

- Requires valid YouTube video with available transcripts
- Depends on Perplexity AI API availability and rate limits
- Transcript quality depends on YouTube's automatic caption accuracy

## 🎯 Use Cases

- **Students**: Create study notes from educational videos
- **Professionals**: Summarize tutorial and training videos
- **Researchers**: Extract key information from academic presentations
- **Content Creators**: Analyze competitor videos and create content summaries

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- Additional features
- Bug fixes
- UI improvements
- Documentation enhancements

## 📄 License

This project is open source and available under the MIT License.

## 👤 About the Developer

**Shabarish B L**
- GitHub: [https://github.com/Shabarish5](https://github.com/Shabarish5)
- LinkedIn: [https://www.linkedin.com/in/shabarish-gowda-039358262](https://www.linkedin.com/in/shabarish-gowda-039358262)

**Profile Summary**:
- Experienced AI and ML Enthusiast with strong academic background
- Data Science Engineering Intern with practical experience in innovative solutions
- Created emotion detection and attendance marking system (AIEmosense)
- Developed personalized voice assistant using natural language processing
- Contributed to crime detection system using ML and computer vision
- Bachelor's degree in Artificial Intelligence and Machine Learning
- Certifications from IBM and Microsoft Azure

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the developer through the provided links.

---

**Note**: Make sure to obtain your own Perplexity AI API key and keep it secure in your `.env` file.

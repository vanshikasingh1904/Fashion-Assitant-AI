# AI Stylist Assistant 👗

A modern AI-powered fashion assistant that provides personalized style recommendations and outfit suggestions using OpenAI's GPT-4 Vision and DALL-E 3.

## Features

- 🎭 **Style Analysis**: Upload your outfit images and get detailed style analysis
- 💫 **Mix & Match**: Get suggestions on how to combine different pieces
- 👗 **AI-Generated Outfits**: View AI-generated outfit suggestions based on your style
- ✨ **Personalized Recommendations**: Share your preferences and get tailored advice
- 🎨 **Modern UI**: Beautiful, responsive interface with glass-morphism design

## Technologies Used

- **Frontend**: Streamlit
- **AI/ML**: OpenAI GPT-4 Vision API, DALL-E 3
- **Image Processing**: Pillow
- **Styling**: Custom CSS with glass-morphism effects

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fashion-assistant-ai.git
   cd fashion-assistant-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file
   - Add your OpenAI API key:
     ```toml
     OPENAI_API_KEY = "your-api-key-here"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter Style Preferences**: Share your style goals, preferences, or specific concerns
2. **Upload Images**: Add images of your outfit pieces
3. **Get Analysis**: Click "Get Personalized Style Advice" to receive:
   - Detailed style analysis for each piece
   - Mixing and matching suggestions
   - AI-generated outfit ideas

## Project Structure

```
fashion-assistant-ai/
├── app.py              # Main application file
├── ui_styles.py        # UI components and styling
├── requirements.txt    # Project dependencies
├── .gitignore         # Git ignore rules
├── .streamlit/        # Streamlit configuration
└── README.md          # Project documentation
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

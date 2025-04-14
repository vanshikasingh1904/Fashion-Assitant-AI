import streamlit as st
from openai import OpenAI
import os
from PIL import Image
import io
import base64
from ui_styles import load_ui_styles, render_header, render_welcome_message, render_section_header, render_analysis_section

# Initialize OpenAI client with API key from Streamlit secrets
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
    base_url="https://api.openai.com/v1"
)

# Page configuration and styling
st.set_page_config(page_title="AI Stylist Assistant", layout="wide")
load_ui_styles()

def analyze_images(images, user_description=None):
    # Convert images to base64
    image_contents = []
    for image in images:
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        image_contents.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{img_str}",
                "detail": "high"
            }
        })
    
    try:
        # Create the analysis prompt based on user input
        prompt = "Analyze these outfits and provide:\n"
        if user_description:
            prompt += f"Taking into account the user's input: '{user_description}'\n"
        prompt += """1. Individual style analysis for each piece
2. How these items could be mixed and matched
3. Specific recommendations addressing any user concerns
4. Suggestions for additional pieces that would complement these items
5. Style tips based on the user's preferences"""

        # Add the text prompt
        image_contents.append({
            "type": "text",
            "text": prompt
        })
        
        # Analyze images using GPT-4.5 Preview
        response = client.chat.completions.create(
            model="gpt-4.5-preview",
            messages=[{
                "role": "user",
                "content": image_contents
            }],
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error analyzing images: {str(e)}")
        return None

def generate_outfit_suggestions(style_description, user_preferences=None):
    try:
        prompt_base = "Create a fashionable outfit suggestion"
        if user_preferences:
            prompt_base += f" considering these preferences: {user_preferences}."
        prompt = f"{prompt_base} Based on: {style_description}. Show a complete outfit on a white background, fashion catalog style."
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response.data[0].url
    except Exception as e:
        st.error(f"Error generating outfit suggestion: {str(e)}")
        return None

def main():
    # Render header
    render_header()

    # Create two columns for the layout
    col1, col2 = st.columns([2, 3])

    with col1:
        # Style preferences input
        render_section_header("Your Style Preferences", "✨")
        user_description = st.text_area(
            "Style Description",
            placeholder="Share your style goals, preferences, or concerns...\n\nExample:\n• I need business casual outfits for a creative office\n• Looking to mix these pieces for different occasions\n• Help me match colors and patterns",
            help="The more details you provide, the more personalized your recommendations will be!",
            height=200,
            label_visibility="collapsed"
        )

        # File uploader
        render_section_header("Upload Your Outfits", "📸")
        uploaded_files = st.file_uploader(
            "Upload Images",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

    with col2:
        if uploaded_files:
            render_section_header("Your Outfits", "🎭")
            # Display uploaded images in a grid
            image_cols = st.columns(min(3, len(uploaded_files)))
            images = []
            
            for idx, uploaded_file in enumerate(uploaded_files):
                image = Image.open(uploaded_file)
                images.append(image)
                with image_cols[idx % 3]:
                    st.image(image, caption=f"Item {idx + 1}", use_container_width=True)
            
            if st.button("✨ Get Personalized Style Advice", use_container_width=True):
                with st.spinner("🎨 Analyzing your style..."):
                    style_analysis = analyze_images(images, user_description)
                    if style_analysis:
                        render_section_header("Your Style Analysis", "💫")
                        render_analysis_section("Style Analysis", style_analysis)
                        
                        render_section_header("AI-Generated Outfit Ideas", "👗")
                        suggestion_cols = st.columns(3)
                        
                        with st.spinner("🎭 Creating outfit suggestions..."):
                            for i, col in enumerate(suggestion_cols):
                                with col:
                                    outfit_url = generate_outfit_suggestions(
                                        f"New outfit suggestion {i+1} inspired by: {style_analysis}",
                                        user_description
                                    )
                                    if outfit_url:
                                        st.image(outfit_url, caption=f"Suggestion {i+1}", use_container_width=True)
        else:
            render_welcome_message()

if __name__ == "__main__":
    main()

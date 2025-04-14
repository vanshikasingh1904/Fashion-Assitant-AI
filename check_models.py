import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# List available models
models = client.models.list()

# Print all model IDs
st.write("Available Models:")
for model in models.data:
    st.write(f"- {model.id}")

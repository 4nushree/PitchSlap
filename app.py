

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PitchSlap", layout="centered")

st.title("🔥 PitchSlap")
st.caption("AI Startup Idea Validator")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

idea = st.text_area(
    "Drop your startup idea 👇 (2–3 lines)",
    placeholder="Eg: AI tool that helps students validate hackathon ideas"
)

if st.button("Validate Idea 🚀") and idea:
    with st.spinner("PitchSlap is thinking..."):
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
You are a startup validator.

Analyze this startup idea:

{idea}

Return:
- Target Customer
- Pain Points
- Monetization
- Competitors
- Why it might fail
- Pivot suggestions
"""

        response = model.generate_content(prompt)
        st.markdown(response.text)

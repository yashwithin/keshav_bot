from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


#LOGICS
model = genai.GenerativeModel("gemini-pro")
def get_idea(query) -> None:
    response = model.generate_content(query)
    return response.text

#ui using streamlit
st.set_page_config(page_title = "SmartBot")
st.header("Keshav Smart Bot")

input = st.text_input("Input: ",key = "input")
submit = st.button("Ask The Question")

if submit:
    response = get_idea(input)
    st.subheader("Your Answer is: ")
    st.write(response)
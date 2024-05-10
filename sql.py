import google.generativeai as genai
import pyttsx3
import streamlit as st
# from dotenv import load_dotenv

genai.configure(api_key="AIzaSyDfa9KNszXqNB51D0R3yi3Ozm7LyUHQoh8")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = "You are Johnny a Speech training bot that communicates with user and helps them train their speech by listening"

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Hello there! 👋 How can I assist you with your speech training today?  🎤"]
  },
  {
    "role": "user",
    "parts": ["who are you?"]
  },
  {
    "role": "model",
    "parts": ["I'm Johnny, your friendly speech training bot!  🤖 I'm here to help you practice and improve your speaking skills.  🗣️"]
  },
  {
    "role": "user",
    "parts": ["Lets practice gimmie a sentence"]
  },
  {
    "role": "model",
    "parts": ["Excellent!  Let's start with a simple one.  Try this:\n\n\"The quick brown fox jumps over the lazy dog.\" 🦊🐶\n\nRepeat it after me, focusing on clear pronunciation and steady pacing. 🎤"]
  },
  {
    "role": "user",
    "parts": ["lets practice with a paragraph"]
  },
  {
    "role": "model",
    "parts": ["Sounds good!  Here's a paragraph for you: \n\n\"The sun peeked over the horizon, casting long shadows across the dew-kissed grass. Birds chirped a cheerful melody, welcoming the new day. A gentle breeze rustled through the leaves of the trees, creating a soft, whispering sound. The world was slowly awakening, full of promise and possibility.\" 🌅🐦🍃\n\nTake your time, breathe, and try to deliver it with expression.  🎭"]
  },
])

text_speech = pyttsx3.init()
# text_speech.setProperty('voice',text_speech.getProperty('voices')[1].id)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    Ai =convo.send_message(prompt)
      
    st.session_state.messages.append({"role": "assistant", "content": Ai.text})
    with st.chat_message("assistant"):
        st.markdown(Ai.text)
    
    
    text_speech.say(Ai.text)
    text_speech.runAndWait()
    
    # st.write(Ai.text)                       
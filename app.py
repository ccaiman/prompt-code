import streamlit as st
import openai

# Title for app
st.title("ChatGPT Code Explorer")

with st.sidebar:
    # Create a slider to control the temperature of the model
    temperature = st.slider("Increase the temperature for wider variations", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.5, 
        step=0.1)
    # Get API key from user
    api_key = st.text_input("Enter your ChatGPT API key:", type="password")

# Get prompt from user
prompt = st.text_area("Enter your free text prompt:", 
                    placeholder="eg: 'write a python script to print hello world'",
                    height=200)

# Set up request to ChatGPT API
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "prompt": prompt,
    "max_tokens": 2048
}

# Submit button
if st.button("Submit"):
    openai.api_key = api_key
    # Send request and get response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=temperature)
    
    # Display response
    st.code(response["choices"][0]["text"])

st.text("Get your own ChatGPT API key at https://openai.com/api/")
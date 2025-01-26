import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "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"



st.title("Samir AI ")
st.write("ИИ на основе Azimov ai")

# Sidebar for user inputs
st.sidebar.title("Settings")
model = st.sidebar.selectbox("Choose model", ["gpt-4o-mini", "gpt-4"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are a helpful assistant."}]

# Input from user
user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get AI response
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=st.session_state["messages"],
            temperature=temperature,
        )
        # Add assistant response to chat history
        message = response["choices"][0]["message"]["content"]
        st.session_state["messages"].append({"role": "assistant", "content": message})
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Type a message and press 'Send'.")

# Display chat history
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**AI:** {message['content']}")

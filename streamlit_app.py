import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

# Set your OpenAI API key


# Streamlit app configuration
st.set_page_config(page_title="Samir AI", layout="centered")

# App title
st.title("🤖 Samir AI")

# Chatbot instructions
st.write("Спрашивай человек. 😊")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are a helpful assistant."}]

# User input
user_input = st.text_input("Вы:", placeholder="Отвечу на все вопросы ...")

# If the user enters a message
if user_input:
    # Append user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Generate response from OpenAI
    with st.spinner("Samir AI думает ..."):
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=st.session_state["messages"])
        reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": reply})

    # Clear the input field
    st.text_input("You:", placeholder="Type your message here...", value="", key="new_input")

# Display chat history
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.write(f"**Samir AI:** {message['content']}")

# Optional: Reset chat history
if st.button("Отправить "):
    st.session_state["messages"] = [{"role": "system", "content": "You are a helpful assistant."}]
    #st.experimental_rerun()

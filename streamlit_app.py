import openai
import streamlit as st
from streamlit import title

st.set_page_config(page_title="Samir AI | DevOps")
openai.api_key = "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"


st.title("Powered by Samir AI")
st.subheader("искусственный интеллект  от https://t.me/bettercallyungways")


user_input = st.text_area("Type here", placeholder="Ask SamirAI | Слышь дядя спрашивай что хочешь я отвечу ")

# Если пользователь отправляет запрос

if st.button("Send request"):
    if user_input.strip():
        try:
          with  st.spinner("Даю ответ"):
            # Запрос к OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # Вы можете использовать "gpt-4", если доступно
                messages=[
                    {"role": "system", "content": "Ты полезный ассистент."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7
            )

            st.spinner("Даю ответ ")
            reply = response['choices'][0]['message']['content']
            st.success("Ответ от Samir AI:")
            st.write(reply)

        except Exception as e:
            st.error(f"Ошибка: {e}")
    else:
        st.warning("[SamirAI] Пожалуйста, введите текст запроса! -> Please ask me ")

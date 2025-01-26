import streamlit as st
import openai
from openai import OpenAI, api_key



client  = OpenAI (api_key = "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")
def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You answer question about Web services."},
                {"role": "user", "content": prompt},
            ],
            temperature=0
        )
        response_dict = response.model_dump()  # <--- convert to dictionary
        response_message = response_dict["choices"][0]["message"]["content"]

        message_content = response["messages"][0]["message"]['content']
    except Exception as e:
        return f"Ошибка при запросе: {e}"

# Интерфейс Streamlit
st.set_page_config(page_title="Samir AI ", layout="centered")
st.title("🤖 Samir AI ")

st.write("ИИ от  @bettercallyungways")

# Поле ввода для пользователя
user_input = st.text_area(" Пишите сюда:", placeholder="Готов ответить на ваш вопрос...")

if st.button("Отправить "):
    if user_input.strip():
        with st.spinner("я думаю ..."):
            response = generate_response(user_input)
        st.markdown(f"### Ответ: \n{response}")
    else:
        st.warning("Пожалуйста, введите запрос!")


st.sidebar.title("О проекте")
st.sidebar.info(
    "Этот сайт создан с использованием Samir AI . \n"
    "Вы можете задавать вопросы, и AI предоставит вам ответы."
)

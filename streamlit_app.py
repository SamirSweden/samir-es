import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

def generate_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        # Использование атрибута для получения ответа
        response_message = completion.choices[0].message.content
        return response_message

    except Exception as e:
        return f"Ошибка при запросе: {e}"

# Интерфейс Streamlit
st.set_page_config(page_title="Samir AI", layout="centered")
st.title("🤖 Samir AI ")

st.write("ИИ от  @bettercallyungways")

# Поле ввода для пользователя
user_input = st.text_area(" Пишите сюда:", placeholder="Готов ответить на ваш вопрос...")

if st.button("Отправить"):
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

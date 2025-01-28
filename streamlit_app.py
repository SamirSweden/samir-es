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

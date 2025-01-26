import streamlit as st
import openai


#openai.api_key = "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"
openai.api_key = "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"
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content']
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

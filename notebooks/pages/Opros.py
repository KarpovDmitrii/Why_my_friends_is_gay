import streamlit as st

st.title("Мы живем в демократической стране")
st.write("Важен голос каждого")
st.write("Пройдите опрос")

st.header("Считаете ли вы Павла гомиком?")
dirs3=['Да', 'Да', 'Да', 'Да', 'Да', 'Да', 'Да', 'Нет']
WindDir3pm = st.selectbox("Гомик??????", dirs3)


button_clicked = st.button("Проголосовать")

if button_clicked:
    st.header("По результатам опроса:")
    st.write("100% проголосовавших выбрали вариант ДА ")
    st.header("Гомопидор №1")
    st.image("data/Pawel3.jpg",width =500)


import streamlit as st
from time import sleep
import pandas as pd

st.title("Цифровая школа")
imag = st.image("schoolis.jpg", width=1920)

import streamlit as st

def definition():
    st.write("### 🔥 Наши курсы")

    # Добавляем стили для контейнера и колонок
    st.markdown("""
        <style>
            .container {
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                background-color: #f9f9f9;
            }
            .course-box {
                padding: 15px;
                border-radius: 10px;
                background: white;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h2 {
                color: #333;
            }
            .form-container {
                text-align: center;
                margin-top: 30px;
            }
            .form-button {
                display: inline-block;
                padding: 12px 20px;
                font-size: 16px;
                color: white;
                background-color: #3A3D86; /* Темно-синий */
                border: none;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
                box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.15);
            }

            .form-button:hover {
                background-color: #2A2D66; /* Темнее при наведении */
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)

    # Основной контейнер
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='course-box'>", unsafe_allow_html=True)
            st.header("💻 Основы программирования")
            st.write("Изучи Python и основы разработки.")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='course-box'>", unsafe_allow_html=True)
            st.header("📚 Подготовка к ЕНТ по информатике")
            st.write("Разбор тестов, подготовка к экзамену.")
            st.markdown("</div>", unsafe_allow_html=True)

def forms_response():
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.header("📩 Оставьте заявку")
    st.write("Заполните форму, и менеджер свяжется с вами в течение дня.")

    # Центрированная кнопка
    st.markdown("""
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <a href="https://forms.gle/gjkbHJLuqrBK5Qt49" class="form-button" target="_blank">
                📝 Заполнить заявку
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Вызываем функции
definition()
forms_response()


# def services():
#     return st.selectbox("Выберите какая страница вам нужна: ", ["Журнал", "Отчеты", "Расписание"])
#
# def show_students():
#     st.header("Просмотр учеников")
#     students = pd.DataFrame(
#         [
#             {"Ученики": "Ученик 1", "Класс": 8, "Оплатил?": True},
#             {"Ученики": "Ученик 2", "Класс": 9, "Оплатил?": True},
#             {"Ученики": "Ученик 3", "Класс": 10, "Оплатил?": False},
#         ]
#     )
#     st.dataframe(students,use_container_width=True)
#
# def show_services(selection):
#     if selection == "Журнал":
#         show_students()
#     else:
#         return st.write("Извините другие функции пока недоступны")

# selection = services()
# show_services(selection)

# name = "Teacher"
# st.title(f'Страница преподавателя {name}')
# k = st.text_input("Вам нужна печать? ")
# # Используем новый способ создания колонок
# imag = st.image("/home/omirzhan/Desktop/dream.jpg")
# # Выводим введенный текст
# def printing(k):
#     if k.lower() == "да":
#         l = st.write("Загрузите флэшку и нажмите кнопку")
#         fast = st.selectbox("Выберите материал: ", ["Силикон", "Пластик"])
#         if fast:
#             bt = st.button("Печать")
#             if bt:
#                 with st.spinner(f'Печатаем материал из {fast}'):
#                     sleep(10)
#                 st.success("Печать сделана")
#     else:
#         m = st.write("Печально")
#
# printing(k)

#
# st.title("🧺 Напоминание о стирке")
# imag = st.image("/home/omirzhan/Desktop/dream.jpg")
# name = st.text_input("Название одежды:")
# fabric = st.selectbox("Выберите тип ткани", ["Хлопок", "Шерсть", "Синтетика", "Деликатное"])
#
# # Генерация рекомендации
# recommendations = {
#     "Хлопок": "Стирка при 40-60°C",
#     "Шерсть": "Стирка при 30°C (деликатный режим)",
#     "Синтетика": "Стирка при 40°C",
#     "Деликатное": "Ручная стирка при 30°C"
# }
#
# if name:
#     st.write(f"👕 {name} → {recommendations[fabric]}")
#
# # Таймер напоминания
# if st.button("Запустить таймер (5 сек для теста)"):
#     with st.spinner("Стираем... ⏳"):
#         sleep(5)
#     st.success("Стирка завершена! Не забудьте достать вещи 😊")
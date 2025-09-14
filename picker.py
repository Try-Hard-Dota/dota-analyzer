import streamlit as st
import json

# Загружаем данные
with open("heroes.json", "r", encoding="utf-8") as f:
    heroes_data = json.load(f)

heroes = [hero["name"] for hero in heroes_data["heroes"]]

st.title("Dota 2 Pick Analyzer 🎮")

st.write("Выбери героев для своей команды:")

# Выбор героев
team = st.multiselect("Твоя команда", heroes, max_selections=5)

# Выбор врагов
enemies = st.multiselect("Враги", heroes, max_selections=5)

# Анализ
if st.button("Анализировать пики"):
    st.subheader("Результаты анализа:")

    if not team and not enemies:
        st.warning("Выбери хотя бы одного героя!")
    else:
        st.write("Твоя команда:", ", ".join(team) if team else "не выбрана")
        st.write("Противники:", ", ".join(enemies) if enemies else "не выбраны")

        # Простейший пример анализа
        if "Axe" in team and "Crystal Maiden" in team:
            st.success("Axe и Crystal Maiden хорошо сочетаются: контроль + массовый урон!")
        if "Juggernaut" in enemies and "Lion" in team:
            st.error("Осторожнее! Lion слаб против Juggernaut.")


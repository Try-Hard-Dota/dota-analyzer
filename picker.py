import streamlit as st
import json

# Загружаем список героев
with open("heroes.json", "r", encoding="utf-8") as f:
    heroes_index = json.load(f)

# Получаем только имена для интерфейса
heroes = [hero["name"] for hero in heroes_index["heroes"]]

st.title("Dota 2 Pick Analyzer 🎮")
team = st.multiselect("Твоя команда", heroes, max_selections=5)
enemies = st.multiselect("Враги", heroes, max_selections=5)

# Анализ
if st.button("Анализировать пики"):
    st.subheader("Результаты анализа:")

    def load_hero(name):
        # находим путь к файлу
        hero_file = next(h["file"] for h in heroes_index["heroes"] if h["name"] == name)
        with open(hero_file, "r", encoding="utf-8") as f:
            return json.load(f)

    team_data = [load_hero(h) for h in team]
    enemy_data = [load_hero(h) for h in enemies]

    team_strength = sum(h.get("strength",0) for h in team_data)
    enemy_strength = sum(h.get("strength",0) for h in enemy_data)

    st.write(f"Сила твоей команды: {team_strength}")
    st.write(f"Сила врагов: {enemy_strength}")

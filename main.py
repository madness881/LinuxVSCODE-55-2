import flet as ft
from datetime import datetime
import random

def main(page: ft.Page):
    page.title = 'Мое первое приложение на Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []
    history_text = ft.Text("История приветствий:")

    names_list = ["Алексей", "Мария", "Иван", "Ольга", "Сергей", "Наталья", "Дмитрий", "Екатерина"]

    def on_button_click(_):
        name = name_input.value.strip()
        now = datetime.now()
        hour = now.hour

        if 6 <= hour < 12:
            greeting_text.value = f"Good morning, {name}!"
        elif 12 <= hour < 18:
            greeting_text.value = f"Good day, {name}"
        elif 18 <= hour < 24:
            greeting_text.value = f"Good evening, {name}"
        else:
            greeting_text.value = "Good night! Please enter a name"

        greet_button.text = "Отправить еще раз"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        greeting_history.append(f'{timestamp} — {name}')
        history_text.value = 'История:\n' + '\n'.join(greeting_history)

        name_input.value = ''
        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def theme_mod(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def fill_random_name(_):
        name_input.value = random.choice(names_list)
        page.update()

    # Кнопки
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=theme_mod)
    clear_button = ft.IconButton(icon_color=ft.Colors.GREEN, icon=ft.Icons.DELETE_FOREVER, tooltip="Очистить историю", on_click=clear_history)

    random_name_button = ft.IconButton(icon=ft.Icons.SHUFFLE, tooltip="Случайное имя", on_click=fill_random_name)

    name_input = ft.TextField(label="Пожалуйста, введите имя: ✍🏻", on_submit=on_button_click)
    greet_button = ft.ElevatedButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)

    # Добавление элементов на страницу
    page.add(
        ft.Row([theme_button, clear_button, random_name_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        greeting_text,
        ft.Row([name_input, greet_button], alignment=ft.MainAxisAlignment.CENTER),
        history_text
    )

ft.app(target=main, view=ft.WEB_BROWSER)

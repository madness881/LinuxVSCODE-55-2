import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    # page.add(ft.Text("Hello world"))
    page.title = 'Мое первое приложение на Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []
    history_text = ft.Text("История приветствий:")

    def on_button_click(_):
        name = name_input.value.strip()

        now = datetime.now()
        hour = now.hour


        if 6 <= hour <=12:
            greeting_text.value = f"Good morning, {name}!"
    
            name_input.value = '  '


            # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # greeting_history.append(f'{timestamp}---{name}')
            # history_text.value = 'History username:\n' + '\n'.join(greeting_history)
        
        elif 12 <= hour <= 18:
            greeting_text.value = f'Good day, {name}'
            
            name_input.value = ' '
        
        elif 18 <= hour < 24:
            greeting_text.value = f'Good evening, {name}'
            name_input.value = ' '
        
        else:
            greeting_text.value = "Good night! Please enter a name" 

        greet_button.text = "Отправить еще раз"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        greeting_history.append(f'{timestamp}---{name}')
        history_text.value = 'История:\n' + '\n'.join(greeting_history) 
        # print(greeting_text.value)
        page.update()
    
    def clear_history(_):
        print("Test")
        greeting_history.clear()
        print(f"История приветствий очищена. {greeting_history}")
        history_text.value = "История приветствий:"
        page.update()

    def theme_mod(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
            
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=theme_mod)
    clear_button = ft.IconButton(icon_color=ft.Colors.GREEN, icon=ft.Icons.DELETE_FOREVER, tooltip="Очистить историю", on_click=clear_history)

    name_input = ft.TextField(label="Plaase enter a name:✍🏻", on_submit=on_button_click)
    greet_button = ft.ElevatedButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)
    # greet_button_1 = ft.TextButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)

    # page.add(theme_button, greeting_text, name_input, greet_button, clear_button, history_text)

    page.add(ft.Row([theme_button, clear_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), 
             greeting_text, 
             ft.Row([name_input, greet_button, history_text], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main, view=ft.WEB_BROWSER)
import flet as ft
from datetime import datetime


def main(page: ft.Page): # создаём главную страницу приложения
    page.title = 'My first app' # заголовок приложения
    page.theme_mode = ft.ThemeMode.LIGHT # устанавливаем тему по умолчанию

    greeting_text = ft.Text('Hello world!') # текст на главной странице
    name_input = ft.TextField(label='Введите имя') # создаём текстовое поле
    greeting_history = []
    history_text = ft.Text('История приветствий: ')


    # def updade_history():
    #     history_controls = [ft.Text('История приветствий: ')]

    def one_button_click(_): # функция для ввода и замены заголовка
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello {name}' # меняем заголовок
            name_input.value = '' # очищаем поле ввода
            timestamp = datetime.now().strftime('%M:%S')

            greeting_history.append(f'{timestamp} - {name}') # фиксируем время ввода
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)

        else:
            print('Ничего не введено')
            greeting_text.value = 'Пожалуйста, введите имя'
        page.update()

    def clear_history(_): # функция для очистки списка
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    def change_theme(_): # функция для смены темы
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode ==  ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()
    
    name_input.on_submit = one_button_click # отправка по enter

    name_button = ft.ElevatedButton('Отправить', on_click=one_button_click) # создаём кнопку
    theme_button = ft.IconButton(icon=ft.Icons.SUNNY, on_click=change_theme)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    # page.add(greeting_text, name_input, name_button, theme_buttom, clear_buttom, history_text) # добавляем элементы на страницу
    page.add(greeting_text, name_input,
              ft.Row([name_button, theme_button, clear_button], alignment=ft.MainAxisAlignment.CENTER),
              history_text
              )


ft.app(target=main) # запуск приложения
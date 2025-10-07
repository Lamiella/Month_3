import flet as ft


def main(page: ft.Page): # создаём главную страницу приложения
    page.title = 'My first app' # заголовок приложения
    page.theme_mode = ft.ThemeMode.LIGHT # устанавливаем тему по умолчанию

    greeting_text = ft.Text('Hello world!') # текст на главной странице
    name_input = ft.TextField(label='Введите имя') # создаём текстовое поле

    def one_button_click(_): # функция для ввода и замены заголовка
        name = name_input.value.strip()
        print(name)

        if name:
            print(greeting_text)
            greeting_text.value = f'Hello {name}' # меняем заголовок
            print(greeting_text)
            name_input.value = '' # очищаем поле ввода
        else:
            print('Ничего не введено')
            greeting_text.value = 'Пожалуйста, введите имя'
        page.update()

    def change_theme(_): # функция для смены темы
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode ==  ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    name_button = ft.ElevatedButton('Отправить', on_click=one_button_click) # создаём кнопку
    theme_buttom = ft.IconButton(icon=ft.Icons.SUNNY, on_click=change_theme)

    page.add(greeting_text, name_input, name_button, theme_buttom) # добавляем элементы на страницу


ft.app(target=main, view=ft.WEB_BROWSER) # запуск приложения
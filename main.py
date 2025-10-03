import flet as ft

def main(page: ft.Page): # создаём главную страницу приложения
    page.title = 'My first app' # заголовок приложения

    greeting_text = ft.Text('Hello world!') # текст на главной странице

    page.add(greeting_text)
    

ft.app(target=main, view=ft.WEB_BROWSER) # запуск приложения
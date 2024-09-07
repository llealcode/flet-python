import flet as ft

def main(page: ft.Page):

    page.window.center()
    page.theme_mode=ft.ThemeMode.DARK
    page.spacing=0
    page.padding=0
    page.window.width = 400
    page.window.height = 400

    titulo = ft.Text(value='Horas extras', size=30, color=ft.colors.WHITE70, weight=ft.FontWeight.W_600)
    txt_salario = ft.TextField()

    container = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                titulo,
                txt_salario
            ]
        ),
        alignment=ft.alignment.center
    )

    page.add(container)

ft.app(target=main)



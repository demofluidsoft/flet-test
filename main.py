import flet as ft


def main(page: ft.Page):


    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

    counter = ft.Text(value="0", size=40)

    def increment(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    def decrement(e):
        counter.value = str(int(counter.value) - 1)
        page.update()

    page.add(
        ft.Column(
            [
                counter,
                ft.Row([
                    ft.ElevatedButton(text="+", on_click=increment),
                    ft.ElevatedButton(text="-", on_click=decrement)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )




ft.app(target=main, view=ft.WEB_BROWSER)

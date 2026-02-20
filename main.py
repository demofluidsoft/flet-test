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
                ft.Row(
                    [
                        ft.Button(text="+", on_click=increment, variant=ft.ButtonVariant.ELEVATED),
                        ft.Button(text="-", on_click=decrement, variant=ft.ButtonVariant.ELEVATED),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# ✅ Use run() now
ft.run(target=main)

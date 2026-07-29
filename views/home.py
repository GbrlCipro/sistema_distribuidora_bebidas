import flet as ft


class HomeView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__()

        self._page = page
        self.expand = True
        self.spacing = 20
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.CENTER

        self.controls = [

            ft.Text(
                'D&D BEBIDAS GELADAS',
                size=32,
                weight=ft.FontWeight.BOLD
            ),

            ft.Container(height=20),

            ft.ElevatedButton(
                content='Consulta de Produtos',
                width=250,
                height=50,
                on_click=lambda e: page.run_task(page.push_route, '/consulta'),
            ),

            ft.ElevatedButton(
                content='Cadastro de Produtos',
                width=250,
                height=50,
                on_click=lambda e: page.run_task(page.push_route, '/produtos'),
            ),
        ]
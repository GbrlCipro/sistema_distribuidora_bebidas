import flet as ft


class ProdutosView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__()

        self._page = page
        self.expand = True
        self.spacing = 20
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.CENTER

        self.controls = [

            ft.Text(
                'Cadastro de Produtos',
                size=28,
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                'Em construção — em breve você poderá cadastrar produtos por aqui.',
                size=14,
                color=ft.Colors.GREY_600,
            ),

            ft.Container(height=20),

            ft.TextButton(
                content='← Voltar',
                on_click=lambda e: page.run_task(page.push_route, '/'),
            ),
        ]
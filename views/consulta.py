import flet as ft
from services.produto_service import buscar_produtos


class ConsultaView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__()

        self._page = page
        self.expand = True
        self.spacing = 20
        
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
        
        # Campo de busca
        self.campo_busca = ft.TextField(
            label='Digite o nome do produto',
            autofocus=True,
            on_change=self.pesquisar  # A MÁGICA ACONTECE AQUI            
        )

        # Área dos resultados
        self.resultados = ft.ListView(
            expand=True,
            spacing=10,
            padding=10,
        )

        self.controls = [

            ft.Row(
                controls=[
                    ft.Text(
                        'Consulta de Produtos',
                        size=28,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.TextButton(
                        content='← Voltar',
                        on_click=lambda e: page.run_task(page.push_route, '/'),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),

            self.campo_busca,

            ft.Divider(),

            self.resultados

        ]

    def pesquisar(self, e):

        texto = self.campo_busca.value.lower().strip()

        self.resultados.controls.clear()

        if not texto:
            self.resultados.controls.append(
                ft.Text('Digite algo para pesquisar.')
            )

        else:

            encontrados = buscar_produtos(texto)

            if encontrados:

                for produto in encontrados:

                    self.resultados.controls.append(

                        ft.Container(

                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        produto.nome,
                                        size=16,
                                        weight=ft.FontWeight.W_600,
                                        expand=True
                                    ),
                                    ft.Text(
                                        f'R$ {produto.preco:.2f}',
                                        size=16,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                ]
                            ),

                            padding=15,
                            border=ft.Border.all(1, '#D0D0D0'),
                            border_radius=10,
                        )
                    )

            else:

                self.resultados.controls.append(
                    ft.Text('Nenhum produto encontrado.')
            )

        self.update()
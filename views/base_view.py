import flet as ft

class BaseView(ft.Stack):
    def __init__(self, content):
        super().__init__(
            expand=True,
            controls=[
                # Camada 1: Fundo sólido base
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.BLACK,
                ),
                
                # Camada 1.1: Imagem com largura total da tela, mas altura controlada/reduzida
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER, # Centraliza verticalmente na tela
                    content=ft.Image(
                        src="background.jpg",
                        width=float("inf"),        # Ocupa 100% da largura horizontal da tela
                        height=1351,                # Altura fixa reduzida (você pode ajustar este valor para mais ou menos)
                        fit="fill",                # Força a imagem a esticar na largura e respeitar a altura menor
                        opacity=0.2,               # Transparência
                    ),
                ),

                # Camada 2: Conteúdo da tela por cima
                ft.Container(
                    expand=True,
                    padding=2,
                    content=content,
                )
            ]
        )
import flet as ft

from database.connections import init_db
from views.base_view import BaseView
from views.home import HomeView
from views.consulta import ConsultaView
from views.produtos import ProdutosView


async def main(page: ft.Page):
    init_db()

    page.title = "D&D BEBIDAS GELADAS"
    page.theme_mode = ft.ThemeMode.DARK

    # Configurações apenas para Desktop
    if not page.web:
        page.window.width = 800
        page.window.height = 600
        await page.window.center()

    def route_change(e):
        page.views.clear()

        # Home
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    BaseView(HomeView(page))
                ],
            )
        )

        # Consulta
        if page.route == "/consulta":
            page.views.append(
                ft.View(
                    route="/consulta",
                    controls=[
                        BaseView(ConsultaView(page))
                    ],
                )
            )

        # Produtos
        elif page.route == "/produtos":
            page.views.append(
                ft.View(
                    route="/produtos",
                    controls=[
                        BaseView(ProdutosView(page))
                    ],
                )
            )

        page.update()

    async def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change(None)


# Desktop
# ft.run(main)

# Web
ft.run(
    main,
    view=ft.AppView.WEB_BROWSER,
    host="0.0.0.0",
    port=8550,
    assets_dir="assets",
)
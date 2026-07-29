# Contexto do Projeto — Sistema de Consulta de Produtos (D&D Bebidas Geladas)

> Documento gerado para dar contexto completo a outra IA/desenvolvedor que for continuar este projeto.
> Última atualização: 19/07/2026

---

## 1. Visão geral do projeto

Sistema desktop para uma **distribuidora de bebidas** (nome fantasia: **D&D Bebidas Geladas**), sediada em Rio Verde, GO, Brasil.

**Escopo atual (fase 1):** apenas consulta de produtos (busca por nome + exibição de preço).
**Escopo futuro (planejado, ainda não iniciado):** cadastro de produtos, controle de estoque, registro de vendas, cadastro de clientes, configurações — a estrutura de pastas já reserva espaço para isso, mas os arquivos ainda estão vazios.

## 2. Stack técnica

- **Linguagem:** Python
- **Framework de UI:** [Flet](https://flet.dev) (usa Flutter por baixo, permite construir apps desktop/mobile/web com UI nativa a partir de Python puro)
- **Banco de dados (planejado, ainda não implementado):** SQLite (`database/produtos.db` existe mas está vazio — sem schema)
- **Padrão arquitetural:** separação em `views/` (UI), `models/` (entidades), `services/` (lógica de negócio) — inspirado em MVC, mas só a camada de views tem conteúdo até agora

### ⚠️ Nota importante sobre a versão do Flet

O projeto já foi atualizado para uma versão recente do Flet que renomeou vários módulos utilitários de **minúsculo (módulo)** para **PascalCase (classe)**. Exemplos confirmados:

| Padrão antigo (não usar) | Padrão novo (usar) |
|---|---|
| `ft.border.all(...)` | `ft.Border.all(...)` |
| `ft.colors.X` | `ft.Colors.X` |
| `ft.icons.X` | `ft.Icons.X` |
| `ft.border_radius.all(...)` | `ft.BorderRadius.all(...)` |

Qualquer código novo ou copiado de tutoriais antigos deve ser adaptado para o padrão PascalCase, ou vai gerar erro `module 'flet.controls.X' has no attribute 'Y'`.

## 3. Estrutura de pastas atual

```
sistema_consulta_produtos/
├── app.py                      → entry point (FUNCIONAL)
├── main.py                     → vazio (não usado; app.py é o entry point real)
├── README.md                   → vazio
├── requirements.txt            → vazio (⚠️ deveria conter "flet" e a versão instalada)
├── database/
│   └── produtos.db             → vazio, sem schema (persistência ainda não implementada)
├── models/
│   ├── cliente.py               → vazio
│   ├── produto.py               → vazio (⚠️ deveria existir uma classe Produto)
│   └── venda.py                 → vazio
├── services/
│   ├── estoque_service.py       → vazio
│   ├── produto_service.py       → vazio (⚠️ lógica de busca hoje está dentro da view, deveria estar aqui)
│   └── venda_service.py         → vazio
└── views/
    ├── consulta.py               → FUNCIONAL (única tela implementada até agora)
    ├── configuracoes.py          → vazio
    ├── estoque.py                → vazio
    ├── home.py                   → vazio
    ├── produtos.py                → vazio
    └── vendas.py                  → vazio
```

## 4. Código atual — `app.py`

```python
import flet as ft
from views.consulta import ConsultaView


def main(page: ft.Page):
    page.title = "D&D BEBIDAS GELADAS"
    page.window.width = 800
    page.window.height = 600
    page.window.center()

    page.theme_mode = ft.ThemeMode.LIGHT

    consulta = ConsultaView(page)

    page.add(consulta)


ft.app(target=main)
```

## 5. Código atual — `views/consulta.py` (estado final, após todos os ajustes)

```python
import flet as ft


class ConsultaView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__()

        self._page = page
        self.expand = True
        self.spacing = 20
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        # Base temporária de produtos (dados hardcoded em memória — sem banco ainda)
        self.produtos = [
            # Refrigerantes e Sucos
            {'nome': 'Coca-Cola 2L', 'preco': 12.00},
            {'nome': 'Coca Zero 2L', 'preco': 13.00},
            {'nome': 'Guaraná Antarctica 2L', 'preco': 10.50},
            {'nome': 'Fanta Laranja 2L', 'preco': 9.50},
            {'nome': 'Sprite 2L', 'preco': 10.00},
            {'nome': 'Schweppes Citrus 1.5L', 'preco': 11.00},
            {'nome': 'Suco Del Valle Uva 1L', 'preco': 8.50},
            {'nome': 'Suco Tang Laranja', 'preco': 1.50},

            # Cervejas e Destilados
            {'nome': 'Heineken Long Neck', 'preco': 9.50},
            {'nome': 'Brahma Duplo Malte', 'preco': 7.00},
            {'nome': 'Cerveja Petra', 'preco': 5.50},
            {'nome': 'Budweiser 330ml', 'preco': 6.50},
            {'nome': 'Corona Extra 330ml', 'preco': 8.50},
            {'nome': 'Skol Lata 350ml', 'preco': 4.00},
            {'nome': 'Whisky Red Label 1L', 'preco': 110.00},
            {'nome': 'Gin Tanqueray 750ml', 'preco': 130.00},
            {'nome': 'Vodka Smirnoff 600ml', 'preco': 45.00},
            {'nome': 'Energético Red Bull 250ml', 'preco': 12.00},

            # Tabacaria
            {'nome': 'Cigarro Marlboro Gold', 'preco': 12.00},
            {'nome': 'Cigarro Lucky Strike', 'preco': 10.00},
            {'nome': 'Isqueiro BIC', 'preco': 6.00},
            {'nome': 'Essência Zomo Mentha', 'preco': 15.00},
            {'nome': 'Carvão p/ Narguilé 1kg', 'preco': 20.00},
            {'nome': 'Papel de Seda OCB', 'preco': 8.00},

            # Básico de Mercado / Conveniência
            {'nome': 'Água Mineral 500ml (c/ gás)', 'preco': 3.50},
            {'nome': 'Água Mineral 500ml (s/ gás)', 'preco': 2.50},
            {'nome': 'Salgadinho Doritos 84g', 'preco': 7.50},
            {'nome': 'Chocolate Bis Ao Leite', 'preco': 6.00},
            {'nome': 'Gelo Cubo 5kg', 'preco': 12.00},
            {'nome': 'Leite Integral 1L', 'preco': 6.50},
            {'nome': 'Pacote de Café 500g', 'preco': 18.00},
            {'nome': 'Pacote de Arroz 5kg', 'preco': 28.00},
        ]

        # Campo de busca
        self.campo_busca = ft.TextField(
            label='Digite o nome do produto',
            autofocus=True,
            on_change=self.pesquisar,  # A MÁGICA ACONTECE AQUI
        )

        # Área dos resultados (ListView, não Column — ver seção de bugs resolvidos)
        self.resultados = ft.ListView(
            expand=True,
            spacing=10,
            padding=10,
        )

        self.controls = [

            ft.Text(
                'Consulta de Produtos',
                size=28,
                weight=ft.FontWeight.BOLD
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

            encontrados = [
                p for p in self.produtos
                if texto in p['nome'].lower()
            ]

            if encontrados:

                for produto in encontrados:

                    self.resultados.controls.append(

                        ft.Container(

                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        produto['nome'],
                                        size=16,
                                        weight=ft.FontWeight.W_600,
                                        expand=True
                                    ),
                                    ft.Text(
                                        f'R$ {produto["preco"]:.2f}',
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

        # Atualiza a tela imediatamente
        self.update()
```

## 6. Funcionalidades já implementadas

- Janela desktop 800x600, centralizada, tema claro, título "D&D BEBIDAS GELADAS"
- Campo de busca com foco automático ao abrir
- Busca em tempo real (`on_change`), sem precisar apertar Enter ou botão
- Filtro case-insensitive por substring no nome do produto
- Lista rolável de resultados, com cards mostrando nome + preço formatado em R$
- Mensagens de estado: "Digite algo para pesquisar" (campo vazio) e "Nenhum produto encontrado" (sem match)
- Base de ~30 produtos de exemplo cobrindo refrigerantes/sucos, cervejas/destilados, tabacaria e itens de conveniência

## 7. Bugs já resolvidos (histórico útil para não repetir o mesmo caminho)

### Bug 1 — `module 'flet.controls.border' has no attribute 'all'`
- **Causa:** versão do Flet instalada já usa API nova (PascalCase). Código usava `ft.border.all(...)` (padrão antigo).
- **Solução:** trocar para `ft.Border.all(...)`.

### Bug 2 — Campo de busca cortado quando a lista de resultados é grande
- **Causa raiz real (só descoberta depois de 3 tentativas):** dois controles com `expand=True` dentro do mesmo `Column` pai dividiam o espaço vertical entre si — o `TextField` (que tinha `expand=True` só para esticar a largura) acabava reservando metade da altura disponível da tela, ficando com espaço vazio abaixo do texto digitado.
- **Tentativas que NÃO resolveram (documentadas para não repetir):**
  1. Adicionar `scroll=ft.ScrollMode.AUTO` + `alignment=ft.MainAxisAlignment.START` no `Column` de resultados — não resolveu porque o problema não estava na área de resultados.
  2. Trocar `Column` por `ListView` na área de resultados — melhoria válida (ListView é mais apropriado para listas roláveis), mas não era a causa do vão.
- **Solução final:**
  1. Remover `expand=True` do `TextField` (`campo_busca`).
  2. Adicionar `self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH` no `Column` principal (a própria `ConsultaView`), para que os filhos ocupem a largura total sem precisar de `expand` individual.
  3. Manter `expand=True` apenas no `ListView` de resultados, que é o único controle que deve crescer verticalmente.
- **Lição aprendida (válida para as próximas telas do projeto):** em um `ft.Column`, `expand` controla o eixo vertical (altura/crescimento) e `horizontal_alignment=STRETCH` controla o eixo horizontal (largura). São propriedades independentes — não usar `expand` como atalho para esticar largura.

## 8. Débitos técnicos / próximos passos identificados

1. **`requirements.txt` vazio** — deveria conter `flet` e a versão exata instalada (rodar `pip show flet` para descobrir).
2. **`database/produtos.db` vazio** — sem schema. Próximo passo natural: criar tabela `produtos` (id, nome, preço, categoria, estoque etc.) e migrar a busca da lista hardcoded em memória para consulta real no SQLite.
3. **`models/produto.py` vazio** — não existe uma classe `Produto`; os dados hoje são dicts soltos. Deveria existir um modelo de dados único antes de integrar com banco.
4. **`services/produto_service.py` vazio** — a lógica de busca está hoje dentro da própria view (`ConsultaView.pesquisar`), misturando UI com regra de negócio. Deveria ser extraída para a camada de service.
5. **`README.md` vazio** — sem documentação do projeto.
6. **Demais views (`home`, `produtos`, `estoque`, `vendas`, `configuracoes`) e demais models/services** — todos vazios, esperando as próximas fases do projeto (fora do escopo atual, que é só consulta).

## 9. Decisões de escopo tomadas pelo usuário

- Foco inicial: **somente consulta de produtos**. Outras funcionalidades (cadastro, estoque, vendas) serão incrementadas depois, uma de cada vez.
- Preferência de trabalho: o usuário faz as edições de código ele mesmo — pediu para não ter os arquivos modificados diretamente, e sim ser guiado (explicações + trechos de código para ele aplicar).

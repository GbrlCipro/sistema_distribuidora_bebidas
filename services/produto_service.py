from database.connections import get_connection
from models.produto import Produto


def buscar_produtos(texto: str) -> list[Produto]:
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM produtos WHERE ativo = 1 AND nome LIKE ? ORDER BY nome",
            (f"%{texto}%",),
        )
        return [Produto.from_row(row) for row in cursor.fetchall()]
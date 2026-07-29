from dataclasses import dataclass


@dataclass
class Produto:
    id: int
    nome: str
    preco: float
    categoria: str | None = None
    estoque: int = 0
    ativo: bool = True

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            nome=row["nome"],
            preco=row["preco"],
            categoria=row["categoria"],
            estoque=row["estoque"],
            ativo=bool(row["ativo"]),
        )
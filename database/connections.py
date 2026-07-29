import sqlite3
import sys
from pathlib import Path


def get_base_path() -> Path:
    if getattr(sys, "frozen", False):
        # Rodando como .exe empacotado — usa a pasta onde o .exe está
        return Path(sys.executable).parent
    else:
        # Rodando como script normal (python app.py)
        return Path(__file__).parent.parent


BASE_PATH = get_base_path()
DB_PATH = BASE_PATH / "database" / "produtos.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
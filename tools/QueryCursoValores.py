from pydantic import Field
from typing import List, Optional
from instructor import OpenAISchema
import sqlite3

class QueryCursoValores(OpenAISchema):
    """Consulta os cursos e valores por semestre ou mensalidade.

        The table schema is:
        CREATE TABLE CursoValores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Curso TEXT,
    Turno TEXT,
    Semestralidade TEXT,
    Mensalidade TEXT,
    Bônus_de_Pontualidade TEXT,
    Mensalidade_Até_o_Vencimento TEXT
);
    """
    query: str = Field(description="Query to be executed in the database")

    def __call__(self, database_path) -> str:
        """Execute the query in the database.

        Args:
            database_path (str): Path to the SQLite database file

        Returns:
            List[dict]: List of students
        """
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        cur.execute(self.query)
        data = cur.fetchall()
        con.close()
        
        return str(data)
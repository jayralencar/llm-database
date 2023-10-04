from pydantic import Field
from typing import List, Optional
from instructor import OpenAISchema
import sqlite3

class QueryCronograma(OpenAISchema):
    """Consulta o cronograma do concurso.

        The table schema is:
        CREATE TABLE Cronograma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATAS TEXT,
            ATIVIDADES TEXT
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
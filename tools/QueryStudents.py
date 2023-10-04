from pydantic import Field
from typing import List, Optional
from instructor import OpenAISchema
import sqlite3

class QueryStudents(OpenAISchema):
    """Query students from the database.

        The table schema is:
        CREATE TABLE student_grades
               (id INTEGER PRIMARY KEY, name TEXT, grade REAL)
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
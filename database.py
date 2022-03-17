import sqlite3
import pandas as pd
from pathlib import Path
import io
import re


dbElements = ['upc', 'format', 'description', 'price']
dataTypes = {'upc': 'str', 'format': 'str', 'description': 'str', 'price': 'float'}
dbPath = Path('db/upcPrice.db')
provided_dbPath = Path('db/upcPrice.txt')
name = 'upc'

class Database:

    # Class initialization
    def __init__(
            self,
            databasePath: Path=dbPath,
            providedDatabasePath: Path=provided_dbPath,
            dbName: str=name,
            normalizeDB: bool=False
    ):
        self.databasePath = databasePath
        self.providedDatabasePath = providedDatabasePath
        self.dbName = dbName

        self.connection = None
        if not self.databasePath.exists() or normalizeDB:
            self.normalizeDB()

        self.connection = self.openDB()
        self.cursor = self.connection.cursor()

    # Class element
    def __del__(self):
        self.closeDB()

    # Class element
    def __enter__(self):
        return self

    # Class element
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closeDB()

    # Open sqlite3 db
    def openDB(self) -> sqlite3.Connection:
        if self.connection is None:
            self.connection = sqlite3.connect(str(self.databasePath))
            self.connection.row_factory = sqlite3.Row
        return self.connection

    # Close sqlite3 db
    def closeDB(self):
        self.cursor.close()
        self.connection.close()

    # Normalize the db in desired format
    def normalizeDB(self):
        output = io.StringIO()
        pattern = re.compile(r'[\b\r]')

        with open(self.providedDatabasePath, 'r', encoding='cp850', newline='\n') as file:
            for line in file:
                output.write(re.sub(pattern, '', line))

        output.seek(0)
        dataframe = pd.read_csv(
            output,
            sep=',',
            names=dbElements,
            dtype=dataTypes,
            engine='python',
            on_bad_lines=fixBadLines
        )
        dataframe.description = dataframe.description.str.strip()
        dataframe.upc = dataframe.upc.str[1:]
        dataframe.to_sql('upc', self.openDB(), index=False, if_exists='replace')
        output.close()

    # Get info about a upc code from db
    def getCodeData(self, upc: str) -> sqlite3.Row:
        self.cursor.execute(f"SELECT * FROM {self.dbName} WHERE upc='{upc}';")
        data = self.cursor.fetchone()
        return data


# Fix bad lines in db
def fixBadLines(line: list[str]) -> list[str]:
    return line[:3] + [line[-1]]

if __name__ == '__main__':
    database = Database(normalizeDB=True)
    print(dict(database.getCodeData("899979495075")))

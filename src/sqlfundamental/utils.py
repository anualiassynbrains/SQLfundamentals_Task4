import os

import urllib
from dotenv import load_dotenv


MYSQL_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@localhost:3306/ecom_db"
POSTGRES_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/ecom_db"
params = urllib.parse.quote_plus(
            f"DRIVER={os.getenv('MSSQL_DRIVER')};"
            f"SERVER={os.getenv('MSSQL_HOST')},{os.getenv('MSSQL_PORT')};"
            f"DATABASE={os.getenv('MSSQL_DB')};"
            f"UID={os.getenv('MSSQL_USER')};"
            f"PWD={os.getenv('MSSQL_PASSWORD')};"
        )

MSSQL_URL = f"mssql+pyodbc:///?odbc_connect={params}"
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import urllib.parse
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Construct database URLs
MYSQL_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@localhost:3306/ecom_db"

POSTGRES_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/ecom_db"
print(POSTGRES_URL)


params = urllib.parse.quote_plus(
    "DRIVER=ODBC Driver 17 for SQL Server;"
    "SERVER=localhost,1433;"
    "DATABASE=ecom_db;"
    "UID=ecom_user;"
    "PWD=AnuAbin25;"
)

MSSQL_URL = f"mssql+pyodbc:///?odbc_connect={params}"

# Load schema.sql
with open("schema.sql", "r") as f:
    schema_sql = f.read()

# Database mapping
DATABASES = {
    "mysql": MYSQL_URL,
    "postgresql": POSTGRES_URL,
    "mssql": MSSQL_URL
}
# engine = create_engine(MYSQL_URL)
# with engine.connect() as conn:
#             for statement in schema_sql.strip().split(';'):
#                 stmt = statement.strip()
#                 if stmt:
#                     conn.execute(text(stmt))
#                     print(f" Schema applied to ")
#                 else:
#                   print(f" Failed to apply schema to")


# # Execute schema on each database
for db_name, db_url in DATABASES.items():
    print(f"\nConnecting to {db_name}...")
    try:
        engine = create_engine(db_url)
        with engine.begin() as conn:  # Use begin() to ensure transaction
            for statement in schema_sql.strip().split(';'):
                stmt = statement.strip()
                if stmt and not stmt.startswith('--'):
                    conn.execute(text(stmt))
        print(f"✅ Schema applied to {db_name}")
    except SQLAlchemyError as e:
        print(f"❌ Failed to apply schema to {db_name}: {e}")


customers_df = pd.read_csv(r"C:\Users\hp\Documents\synbrains_trainee_works\sqlwork\customers.csv")
products_df = pd.read_csv(r"C:\Users\hp\Documents\synbrains_trainee_works\sqlwork\products.csv")
orders_df = pd.read_csv(r"C:\Users\hp\Documents\synbrains_trainee_works\sqlwork\orders.csv")

dataframes = {
    "customers": customers_df,
    "products": products_df,
    "orders": orders_df
}

for db_name, db_url in DATABASES.items():
    print(f"\n📦 Inserting data into {db_name}...")
    try:
        engine = create_engine(db_url)
        conn = engine.connect()
        for table_name, df in dataframes.items():
            
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            count = result.scalar()
            if count == 0:
                df.to_sql(table_name, con=conn, if_exists='append', index=False)
                print(f"✅ Inserted into {table_name}")
            else:
                print(f"⚠️ Skipped {table_name}: table already contains {count} rows")
        conn.close()
    except Exception as e:
        print(f"❌ Failed to insert into {db_name}: {e}")


db_name=['MYSQL','POSTGRES','SQL']
for name in db_name:
  if name=='MYSQL':
    engine=create_engine(MYSQL_URL)
    conn=engine.connect()
    query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, city FROM customers;"
    electronicquery="SELECT * FROM products WHERE category = 'Electronics';"
    result = conn.execute(text(query))
    electronicresult=conn.execute(text(electronicquery))
    
    for value in result:
        print(value)

  if name=='POSTGRES':
    engine=create_engine(POSTGRES_URL)
    conn=engine.connect()
    query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, city FROM customers;"
    result = conn.execute(text(query))
    print(result)
    for value in result:
        print(value)



  if name=='SQL':
    engine=create_engine(POSTGRES_URL)
    conn=engine.connect()
    query = "SELECT first_name + ' ' + last_name AS full_name, city FROM customers;"
    result = conn.execute(text(query))
    print(result)
    for value in result:
        print(value)
  
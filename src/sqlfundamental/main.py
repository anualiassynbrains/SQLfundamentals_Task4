import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import urllib.parse
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
import pandas as pd

# Load environment variables from .env file
load_dotenv()
import argparse
from utils import MYSQL_URL,POSTGRES_URL,MSSQL_URL


class DatabaseIntegration:
    def __init__(self,targetdatabase,questionnumber):
        self.targetdatabase=targetdatabase
        self.questionnumber=questionnumber
        self.create_tables(self.targetdatabase)
        self.add_data(self.targetdatabase)
        self.query_execution(self.targetdatabase,self.questionnumber)

    def create_tables(self,targetdatabase):
        self.MYSQL_URL = MYSQL_URL
        self.POSTGRES_URL = POSTGRES_URL
        
        self.MSSQL_URL = MSSQL_URL
        with open("schema.sql", "r") as f:
           schema_sql = f.read()
           if targetdatabase=='mysql':
                try:
                    engine = create_engine(self.MYSQL_URL)
                    with engine.begin() as conn:  
                            for statement in schema_sql.strip().split(';'):
                                stmt = statement.strip()
                                if stmt and not stmt.startswith('--'):
                                    conn.execute(text(stmt))
                            print(f" Schema applied to mysql")
                except SQLAlchemyError as e:
                        print(f" Failed to apply schema to mysql: {e}")

           if targetdatabase=='postgres':
                try:
                    engine = create_engine(self.POSTGRES_URL)
                    with engine.begin() as conn:  
                            for statement in schema_sql.strip().split(';'):
                                stmt = statement.strip()
                                if stmt and not stmt.startswith('--'):
                                    conn.execute(text(stmt))
                            print(f" Schema applied to POSTGRES")
                except SQLAlchemyError as e:
                        print(f" Failed to apply schema to POSTGRES: {e}")

           if targetdatabase=='mssql':
                try:
                    engine = create_engine(self.MSSQL_URL)
                    with engine.begin() as conn:  
                            for statement in schema_sql.strip().split(';'):
                                stmt = statement.strip()
                                if stmt and not stmt.startswith('--'):
                                    conn.execute(text(stmt))
                            print(f" Schema applied to MSSQL")
                except SQLAlchemyError as e:
                        print(f" Failed to apply schema to MSSQL: {e}")

    def add_data(self,targetdatabase):
            customers_df = pd.read_csv(r"C:\Users\hp\Documents\synbrains_trainee_works\sqlwork\customers.csv")
            products_df = pd.read_csv(r"C:\Users\hp\Documents\synbrains_trainee_works\sqlwork\products.csv")
            orders_df = pd.read_csv(r"C:\Users\hp\Documents\synbrains_trainee_works\sqlwork\orders.csv")

            dataframes = {
                "customers": customers_df,
                "products": products_df,
                "orders": orders_df
             }
            if targetdatabase=='mysql':
                 try:
                    engine = create_engine(self.MYSQL_URL)
                    conn = engine.connect()
                    for table_name, df in dataframes.items():
                        # Check if the table is empty
                        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                        count = result.scalar()
                        if count == 0:
                            df.to_sql(table_name, con=conn, if_exists='append', index=False)
                            print(f" Inserted into {table_name}")
                        else:
                            print(f" Skipped {table_name}: table already contains {count} rows")
                    conn.close()
                 except Exception as e:
                    print(f" Failed to insert into mysql: {e}")

            if targetdatabase=='postgres':
                 try:
                    engine = create_engine(self.POSTGRES_URL)
                    conn = engine.connect()
                    for table_name, df in dataframes.items():
                        # Check if the table is empty
                        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                        count = result.scalar()
                        if count == 0:
                            df.to_sql(table_name, con=conn, if_exists='append', index=False)
                            print(f" Inserted into {table_name}")
                        else:
                            print(f" Skipped {table_name}: table already contains {count} rows")
                    conn.close()
                 except Exception as e:
                    print(f" Failed to insert into postgres: {e}")

            if targetdatabase=='mssql':
                 try:
                    engine = create_engine(self.MSSQL_URL)
                    conn = engine.connect()
                    for table_name, df in dataframes.items():
                        
                        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                        count = result.scalar()
                        if count == 0:
                            df.to_sql(table_name, con=conn, if_exists='append', index=False)
                            print(f" Inserted into {table_name}")
                        else:
                            print(f" Skipped {table_name}: table already contains {count} rows")
                    conn.close()
                 except Exception as e:
                    print(f" Failed to insert into mssql: {e}")




    def query_execution(self,targetdatabse,question_number):
         if question_number==1:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, city FROM customers;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, city FROM customers;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, city FROM customers;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)



         if question_number==2:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM products WHERE category = 'Electronics';"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM products WHERE category = 'Electronics';"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM products WHERE category = 'Electronics';"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


         if question_number==3:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM orders WHERE quantity > 1;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM orders WHERE quantity > 1;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM orders WHERE quantity > 1;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


         if question_number==4:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM products ORDER BY price DESC;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM products ORDER BY price DESC;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT * FROM products ORDER BY price DESC;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

         if question_number==5:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT o.order_id,c.first_name,p.product_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT o.order_id,c.first_name,p.product_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT o.order_id,c.first_name,p.product_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)
                   
         if question_number==6:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT c.first_name, COUNT(o.order_id) AS order_count FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.first_name;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT c.first_name, COUNT(o.order_id) AS order_count FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.first_name;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT c.first_name, COUNT(o.order_id) AS order_count FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.first_name;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

         if question_number==7:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT p.product_name, SUM(o.quantity * p.price) AS total_revenue FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_name;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT p.product_name, SUM(o.quantity * p.price) AS total_revenue FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_name;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT p.product_name, SUM(o.quantity * p.price) AS total_revenue FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_name;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

         if question_number==8:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name,SUM(o.quantity * p.price) AS total_spending FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id GROUP BY c.customer_id, c.first_name, c.last_name ORDER BY total_spending DESC;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name,SUM(o.quantity * p.price) AS total_spending FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id GROUP BY c.customer_id, c.first_name, c.last_name ORDER BY total_spending DESC;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name,SUM(o.quantity * p.price) AS total_spending FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id GROUP BY c.customer_id, c.first_name, c.last_name ORDER BY total_spending DESC;"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)



         if question_number==9:
              if targetdatabse=='mysql':
                    engine=create_engine(self.MYSQL_URL)
                    conn=engine.connect()
                    query = "SELECT c.first_name,c.last_name,p.product_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id WHERE c.city = 'London';"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)

              if targetdatabse=='postgres':
                    engine=create_engine(self.POSTGRES_URL)
                    conn=engine.connect()
                    query = "SELECT c.first_name,c.last_name,p.product_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id WHERE c.city = 'London';"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)


              if targetdatabse=='mssql':
                    engine=create_engine(self.MSSQL_URL)
                    conn=engine.connect()
                    query = "SELECT c.first_name,c.last_name,p.product_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id WHERE c.city = 'London';"
                    result = conn.execute(text(query))
                    for value in result:
                         print(value)
                   
                  

         
                
               

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run SQL integration by database and question number.")
    
    parser.add_argument(
        "--db", 
        type=str, 
        required=True, 
        choices=["mysql", "postgres", "mssql"],
        help="Target database (mysql, postgres, mssql)"
    )
    
    parser.add_argument(
        "--question", 
        type=int, 
        required=True, 
        choices=range(1, 10),
        help="Question number (1 to 9)"
    )

    args = parser.parse_args()

   
    DatabaseIntegration(targetdatabase=args.db, questionnumber=args.question)

Multi-Database SQL Integration with Command-Line Interface
==========================================================

This project allows you to create tables, load data from CSV files, and run SQL queries across multiple databases (MySQL, PostgreSQL, and MS SQL Server) using a simple Python command-line interface.

Features
--------

*   Universal schema creation using standard SQL.
    
*   Automatic data loading from CSV files.
    
*   Supports MySQL, PostgreSQL, and MS SQL Server.
    
*   Query execution for questions 1 through 9 via CLI.
    
*   Uses argparse for command-line control.
    

Prerequisites
-------------

*   Python 3.8+
    
*   Poetry (optional, for dependency management)
    
*   MySQL, PostgreSQL, and SQL Server installed locally (or remotely accessible)
    
*   ODBC Driver 17 for SQL Server (for MSSQL)
    

Installation
------------

1.  Clone the repository:  
    git clone [https://github.com/anualiassynbrains/SQLfundamentals\_Task4.git](https://github.com/anualiassynbrains/SQLfundamentals_Task4.git)  
    cd SQLfundamentals\_Task4
    
2.  Set up your environment:  
    pip install -r requirements.txt
    
3.  Create a `.env` file with the following content:
    

  

`# MySQL
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password

# PostgreSQL
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password

# SQL Server
MSSQL_USER=your_mssql_user
MSSQL_PASSWORD=your_mssql_password
MSSQL_HOST=localhost
MSSQL_PORT=1433
MSSQL_DB=ecom_db
MSSQL_DRIVER=ODBC Driver 17 for SQL Server` 

Usage
-----

Run from the command line:

python main.py --db postgres --question 7

\--db : Target database (mysql, postgres, or mssql)  
\--question : Question number (1 to 9)

Example:

python main.py --db mysql --question 3

This will:

*   Apply the schema to MySQL
    
*   Load the CSV data (if not already inserted)
    
*   Run the SQL query for Question 3
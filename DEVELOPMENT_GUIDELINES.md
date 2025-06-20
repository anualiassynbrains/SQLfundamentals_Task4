DEVELOPMENT GUIDELINES
======================

This guide explains how to set up three local database systems — MySQL, PostgreSQL, and Microsoft SQL Server — without using Docker. It also covers how to configure a Python project using Poetry and how to manage credentials securely using a `.env` file.

* * *

Prerequisites
-------------

*   OS: Windows, macOS, or Linux
    
*   Admin rights to install software
    
*   Python 3.10+ installed
    

* * *

1\. MySQL Setup
---------------

### Installation

1.  Download the MySQL Installer from [https://dev.mysql.com/downloads/installer](https://dev.mysql.com/downloads/installer)
    
2.  Run the installer and select:
    
    *   MySQL Server
        
    *   MySQL Workbench
        
3.  During setup:
    
    *   Choose "Standalone MySQL Server"
        
    *   Set a secure root password
        
    *   Enable the server to start automatically
        

### Create Database and User

Open MySQL Workbench or the terminal and run:


`CREATE DATABASE ecom_db;
CREATE USER 'ecom_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON ecom_db.* TO 'ecom_user'@'localhost';
FLUSH PRIVILEGES;` 

* * *

2\. PostgreSQL Setup
--------------------

### Installation

1.  Download the installer from [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
    
2.  Run the installer:
    
    *   Set a password for the default `postgres` user
        
    *   Install pgAdmin if you want a GUI
        

### Create Database and User

Open pgAdmin 1.  Right-click on **Databases** → click **Create → Database...**
    
2.  Fill in:
    
    *   **Database name**: `ecom_db`
        
    *   **Owner**: `postgres` (default — you can change later)
        
3.  Click **Save**
    

✅ Your `ecom_db` database is now created.

* * *

### 👤 Step 3: Create the `ecom_user` Role (User)

1.  In the left panel, expand:
    
    pgsql
    
    CopyEdit
    
    `Servers → PostgreSQL → Login/Group Roles` 
    
2.  Right-click **Login/Group Roles** → click **Create → Login/Group Role...**
    
3.  In the **General** tab:
    
    *   Name: `ecom_user`
        
4.  In the **Definition** tab:
    
    *   Set a **password** and confirm it
        
5.  In the **Privileges** tab:
    
    *   Toggle **Can login?** to `Yes`
        
6.  Click **Save**
    

✅ The `ecom_user` role is now created.

* * *

3\. Microsoft SQL Server Setup
------------------------------

### Installation

1.  Download the SQL Server Developer Edition from [https://www.microsoft.com/en-us/sql-server/sql-server-downloads](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
    
2.  During setup:
    
    *   Select "Developer Edition"
        
    *   Enable "Mixed Mode Authentication"
        
    *   Set a secure password for the `sa` account
        

### Install SQL Server Management Studio (SSMS)

Download from https://aka.ms/ssms

### Create Database and User

Open SSMS and run the following SQL:





`CREATE DATABASE ecom_db;
GO

CREATE LOGIN ecom_user WITH PASSWORD = 'your_secure_password';
GO

USE ecom_db;
CREATE USER ecom_user FOR LOGIN ecom_user;
ALTER ROLE db_owner ADD MEMBER ecom_user;
GO` 

* * *

4\. Python Environment Setup with Poetry
----------------------------------------

### Install Poetry

Run the following command:

nginx

CopyEdit

`pip install poetry` 

For alternative installation methods, visit https://python-poetry.org/docs/#installation

### Create a New Project

arduino

CopyEdit

`poetry new ecom_project
cd ecom_project
poetry shell` 

### Add Required Dependencies

Install required packages to connect to the databases and manage environment variables:

sql

CopyEdit

`poetry add pymysql psycopg2-binary pyodbc python-dotenv` 

* * *

5\. Credential Management with .env
-----------------------------------

### Create a `.env` File in Your Project Root

ini

CopyEdit

`MYSQL_USER=ecom_user
MYSQL_PASSWORD=your_secure_password
MYSQL_DB=ecom_db

POSTGRES_USER=ecom_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=ecom_db

MSSQL_USER=ecom_user
MSSQL_PASSWORD=your_secure_password
MSSQL_DB=ecom_db` 

### Load Environment Variables in Python

Example code to load the credentials:

python

CopyEdit

`from dotenv import load_dotenv
import os

load_dotenv()

mysql_user = os.getenv("MYSQL_USER")
postgres_user = os.getenv("POSTGRES_USER")
mssql_user = os.getenv("MSSQL_USER")` 

Important: Always add `.env` to your `.gitignore` file to prevent accidentally uploading sensitive credentials to version control.

* * *

Summary
-------

Database

DB Name

User

Authentication

MySQL

ecom\_db

ecom\_user

Localhost + Password

PostgreSQL

ecom\_db

ecom\_user

Role + Password

MS SQL Server

ecom\_db

ecom\_user

SQL Login + db\_owner

With all databases configured and the Python project ready with Poetry, you're now fully set up for development.
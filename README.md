# PostgreSQL-Using-Python-Project

This project was developed to test my knowledge of creating & connecting to a PostgreSQL (pssql) database using Python. The purpose of this upload, is to teach aspiring data
students/professionals how to create a database, connect to it and insert data from a dataset into a PostgreSQL database only using Python.

## Prerequisites:
* Install PostgreSQL: https://www.postgresql.org/download/  (During the installation process, remember to keep track of the password you created)
* Install Python Onto Your IDE (VS Code, PyCharm, etc.): https://www.python.org/ (During the installation process click checkbox ADD TO PATH)
OR
* If you can't install an IDE + Python, you can use a free online source called jupyter notebook: https://jupyter.org/try

## Step 1
Once PostgreSQL is installed on your system, open the PostgreSQL Folder in your program list, and open the SQL shell (psql) command line interface. Complete Steps listed below:
Server [localhost]: **press ENTER (this is a default setting)**
Database [postgres]: **press ENTER (this is the default database)**
Port [5432]: **press ENTER (this is the default port #)**
Username [postgres]: **press ENTER (this is the default username)**
Password for user postgres: **use the password you created during the installation process**

IF YOU SEE THIS TEXT BELOW, THIS MEANS THAT YOU HAVE CONNECTED TO THE DEFAULT POSTGRESQL DATABASE called: postgres. 👍 Now minimize this tab.

psql (14.2)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=#

## Step 2
Find any dataset that you find interesting (you can use the following sites to assist you):
# https://www.kaggle.com/
# https://registry.opendata.aws/

## Step 3
#If Using An IDE:
Open your terminal and type `!pip install psycopg2`  Note: We're using psycopg2, b/c it is the most popular PostgreSQL database adapter for Python

#If Using jupyter notebook:
Type `!pip install psycopg2` and click run










from distutils.log import error
from distutils.util import execute
from msilib.schema import Error
from sqlite3 import connect
import psycopg2

###     Creating a connection to the database (postgres)  ###
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=9296547")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

###    Use connection to get a cursor that can be used to exceute queries unto the database  ###
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to database")
    print(e)

###   Assign autocommit to true so that each action is committed without having to call conn.commit() after each command  ###
conn.set_session(autocommit=True)




###   Creating a database   ###
try:
    cur.execute("create database myfirstdb") #this string is SQL syntax to create a database (CREATE DATABSE _____)
except psycopg2.Error as e:
    print(e)

###   Creating a connection to the database (myfirstdb) ###
try:
    conn.close() #closing the current db (postgres) connection
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect("host=localhost dbname=myfirstdb user=postgres password=9296547")
except psycopg2.Error as e:
    print("Error: Could not make connection to myfirstdb database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print(e)

conn.set_session(autocommit=True)

###  Creating a database for Amazon_Products
## uniq_id
## product_name
## manafacturer
## price
## number_available
## number_of_reviews
## number_of_answered_questions
## average_review_rate
## amazon_category
## description


###  Creating table for Amazon_Products
try:
    cur.execute("CREATE TABLE IF NOT EXISTS Amazon_Products (uniq_id varchar, product_name text, manafacturer varchar, price float, number_available int, number_of_reviews int, number_of_answered_questions int, average_review_rate float, amazon_category text, description text);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

###  Inserting Two Rows of Data Manually ###

## ROW 1 ##
try:
    cur.execute("INSERT INTO Amazon_Products (uniq_id, product_name, manafacturer, price, number_available, number_of_reviews, number_of_answered_questions, average_review_rate, amazon_category, description) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                 ("eac7efa5dbd3d667f26eb3d3ab504464", "Hornby 2014 Catalogue", "Hornby", 3.42, 5, 15, 1, 4.9, "Hobbies > Model Trains & Railway Sets > Rail Vehicles > Trains", "Product Description Hornby 2014 Catalogue Box Contains 1 x one catalogue"))
except psycopg2.Error as e:
    print("Error: Could not insert row into database")
    print(e)        

## ROW 2 ##
try:
    cur.execute("INSERT INTO Amazon_Products (uniq_id, product_name, manafacturer, price, number_available, number_of_reviews, number_of_answered_questions, average_review_rate, amazon_category, description) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                ("b17540ef7e86e461d37f3ae58b7b72ac", "FunkyBuys® Large Christmas Holiday Express Festive Train Set (SI-TY1017) Toy Light / Sounds / Batteries", "FunkyBuys", 16.99, 0, 2, 1, 4.5, "Hobbies > Model Trains & Railway Sets > Rail Vehicles > Trains", "Size Name:Large FunkyBuys® Large Christmas Holiday Express Festive Train Set (SI-TY1017) Toy Light"))
except psycopg2.Error as e:
    print("Error: Could not insert row into database")
    print(e)

### Validating That My Data Was Inserted Into the Table ###
try:
    cur.execute("SELECT * FROM Amazon_Products;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone() #function will pull the first row from the table Amazon_Products
while row:
    print(row) #will print row of data
    row = cur.fetchone()


### Closing Cursor and Connection ###
cur.close()
conn.close()
# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd


# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql_query("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)


# STEP 3
# Reverse the column order
df_five_reverse = pd.read_sql_query("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)


# STEP 4
# Alias employeeNumber as ID
df_alias = pd.read_sql_query("""
    SELECT employeeNumber AS ID, lastName
    FROM employees
""", conn)


# STEP 5
# Use CASE to identify executives
df_executive = pd.read_sql_query("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
                OR jobTitle LIKE '%Manager%'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# STEP 6
# Calculate the length of the employee's full name
df_name_length = pd.read_sql_query("""
    SELECT firstName, lastName,
           LENGTH(firstName || lastName) AS name_length
    FROM employees
""", conn)


# STEP 7
# Get the first two characters of the job title
df_short_title = pd.read_sql_query("""
    SELECT jobTitle,
           SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)


# STEP 8
# Calculate the total price
sum_total_price = pd.read_sql_query("""
    SELECT SUM(priceEach) AS total_price
    FROM orderdetails
""", conn).values[0]


# STEP 9
# Extract day, month, and year from order date
df_day_month_year = pd.read_sql_query("""
    SELECT
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders
""", conn)
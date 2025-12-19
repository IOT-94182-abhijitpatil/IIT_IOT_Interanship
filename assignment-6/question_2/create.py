# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = " smart_agri ",
    use_pure = True
)

# form a query to be executed
ID = int(input("Enter sensor_ID : "))
moisture_level = float(input("Enter moisture_level : "))
reading_time = input("Enter reading_time : ")

query = f"insert into soil_moisture_readings values({ID}, {moisture_level}, '{reading_time}');"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()


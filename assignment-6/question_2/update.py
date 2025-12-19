# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri",
    use_pure = True
)

# form a query to be executed
ID = (input("Enter sensor_ID whose moisture_level to be updated  : "))
moisture_level = (input("Enter new moisture_level : "))

query = f"update soil_moisture_readings SET moisture_level = {moisture_level} where sensor_ID = {ID};"

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

